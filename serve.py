"""Local dev server with HTTP Range support. python -m http.server answers no
Range requests, so the hero mp4 never loads locally (see ERRORS.md).
Usage: python serve.py [port]   (serves this folder)"""
import os, re, sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Range(SimpleHTTPRequestHandler):
    def send_head(self):
        m = re.match(r"bytes=(\d+)-(\d*)", self.headers.get("Range") or "")
        path = self.translate_path(self.path)
        if not m or os.path.isdir(path):
            return super().send_head()
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(404)
            return None
        size = os.fstat(f.fileno()).st_size
        start = int(m.group(1))
        end = min(int(m.group(2)) if m.group(2) else size - 1, size - 1)
        if start > end:
            f.close()
            self.send_error(416)
            return None
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", "bytes %d-%d/%d" % (start, end, size))
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        f.seek(start)
        return _Capped(f, end - start + 1)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


class _Capped:
    """Hands the server only the bytes inside the requested range."""
    def __init__(self, f, n):
        self.f, self.n = f, n

    def read(self, size=-1):
        if self.n <= 0:
            return b""
        size = self.n if size is None or size < 0 or size > self.n else size
        data = self.f.read(size)
        self.n -= len(data)
        return data

    def close(self):
        self.f.close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8643
    root = os.path.dirname(os.path.abspath(__file__))
    ThreadingHTTPServer(("127.0.0.1", port), partial(Range, directory=root)).serve_forever()
