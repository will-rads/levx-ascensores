// Run: node --test hero.test.cjs
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync(require('node:path').join(__dirname, 'script.js'), 'utf8');
const code = source.slice(source.indexOf('if (noMotion) {'), source.indexOf('/* Service panels:'));
function setup(noMotion = false) {
  let tick, observer, deadline;
  const events = {}, seeks = [], classes = new Set();
  let time = 0;
  const video = { duration: 10, readyState: 1, seeking: false, muted: true,
    pause() {}, play() { return Promise.resolve(); },
    addEventListener(n, f) { events[n] = f; },
    get currentTime() { return time; },
    set currentTime(t) { seeks.push(t); time = t; }
  };
  const copy = { style: {}, inert: true };
  runInNewContext(code, { noMotion, heroVideo: video, heroCopy: copy,
    heroCue: { style: {} }, hero: { offsetHeight: 2800, classList: { add: x => classes.add(x) },
      querySelector: () => ({ offsetHeight: 1000 }), getBoundingClientRect: () => ({ top: -900 }) },
    window: { addEventListener() {} },
    setTimeout: f => { deadline = f; return 1; }, clearTimeout() {},
    requestAnimationFrame: f => { tick = f; return 1; }, cancelAnimationFrame() {},
    IntersectionObserver: class { constructor(f) { observer = f; } observe() {} },
  });
  return { video, seeks, classes, copy, events, start: () => observer([{ isIntersecting: true }]),
    tick: t => tick(t), timeout: () => deadline() };
}
test('metadata-only video seeks, without overlapping or redundant seeks', () => {
  const s = setup(); s.start(); s.tick(0);
  assert.equal(s.seeks.length, 1); assert.ok(Math.abs(s.seeks[0] - 4.97) < 0.001);
  s.video.currentTime = 0; s.seeks.length = 0; s.video.seeking = true; s.tick(100);
  assert.equal(s.seeks.length, 0);
  s.video.seeking = false; s.tick(110); assert.equal(s.seeks.length, 1);
  s.tick(200); assert.equal(s.seeks.length, 1);
});
test('failed load exposes a usable static hero', () => {
  const s = setup(); s.timeout();
  assert.ok(s.classes.has('no-scrub')); assert.equal(s.copy.inert, false);
  assert.equal(s.copy.style.opacity, 1);
});
test('reduced motion stays static', () => assert.ok(setup(true).classes.has('no-scrub')));
