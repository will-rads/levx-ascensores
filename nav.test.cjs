const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync(require('node:path').join(__dirname, 'script.js'), 'utf8');
test('navigation highlight follows focus, selection and resized links', () => {
  const pill = { style: {} }, handlers = {};
  const links = [5, 92, 173].map((offsetLeft, i) => ({ offsetLeft, offsetWidth: 80,
    hash: '#' + i, handlers: {}, classList: { toggle() {} },
    addEventListener(n, fn) { this.handlers[n] = fn; } }));
  const nav = { offsetWidth: 260, querySelectorAll: () => links, querySelector: () => pill,
    addEventListener(n, fn) { handlers[n] = fn; } };
  let resize;
  runInNewContext(source.slice(source.indexOf('/* Floating navigation:'), source.indexOf('/* Hero intro:')), {
    document: { querySelector: s => s === '.main-nav' ? nav : {}, activeElement: null },
    ResizeObserver: class { constructor(fn) { resize = fn; } observe() {} },
    IntersectionObserver: class { observe() {} },
  });
  resize(); assert.equal(pill.style.transform, 'translateX(5px)');
  links[2].handlers.focus(); assert.equal(pill.style.transform, 'translateX(173px)');
  links[2].handlers.click(); handlers.pointerleave();
  assert.equal(pill.style.transform, 'translateX(173px)');
  links[2].offsetWidth = 110; resize(); assert.equal(pill.style.width, '110px');
  nav.offsetWidth = 0; resize(); assert.equal(pill.style.opacity, 0);
});
