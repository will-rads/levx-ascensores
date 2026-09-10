# Operational notes

## Git account

Default GitHub CLI credentials select NamouProperties, which cannot push this repository. The stored personal credential is in Git Credential Manager. Use this per-command override from the repository:

```powershell
git -c credential.helper= -c credential.helper=manager -c credential.username=will-rads push origin main
```

The personal CLI wrapper is `../../.codex-tools/github-cli/Invoke-GhWillRads.ps1`. Never print credential values. A sandbox credential error may require running the authorized push outside the sandbox.

## Domain DNS

Hostinger rejected converting the old root ALIAS directly to A. Replacing it resolved the conflict; DNS history has restore points. Preserve mail records and nameservers. Because root redirects to www, a pending www certificate can block both addresses. Both certificates subsequently completed; do not bypass certificate warnings.

## Video and browser checks

- The live MP4 supports HTTP Range requests (206 verified). A basic Python server does not provide equivalent seek behavior.
- The existing 3.5 MB clip is H.264/yuv420p, 1600x900, 24fps, all keyframes. No separate mobile asset is needed.
- Preload is a browser hint. Avoid overlapping seeks, keep muted/inline loading priming, and preserve the static load-error fallback.
- Verify real MacBook behavior separately from Windows browser tests and phone-size emulation.

## Code traps

- Call `setLang` after `VOICES` and review helpers exist; otherwise initialization can fail.
- Keep Satoshi and Gambarino in separate Fontshare links; combined requests previously omitted Gambarino.
- Use IntersectionObserver/rAF for scroll effects; preserve reduced-motion handling.
- Service photos change brightness/contrast, not saturation. Small manufacturer logos use opacity rather than blur.

## Superseded

The mobile tilted deck and its RTL positioning workaround were replaced by horizontal rows. Earlier repo-creation and Vercel project-creation workarounds are no longer part of routine deployment; push the existing repository instead.
