// Run: node --test reviews.test.cjs
const { test } = require("node:test");
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { runInNewContext } = require("node:vm");
const source = readFileSync(require("node:path").join(__dirname, "script.js"), "utf8");
const render = source.slice(source.indexOf("function renderVoices(dict)"), source.indexOf("/* Marquee: duplicate"));

for (const still of [false, true]) {
  test(`review rows, reduced motion: ${still}`, () => {
    const voiceRows = [{}, {}];
    const voiceCols = Array.from({ length: 3 }, () => ({ style: {}, dataset: { speed: "46" } }));
    runInNewContext(render + "renderVoices({});", {
      still, voiceRows, voiceCols,
      VOICES: Array.from({ length: 9 }, (_, id) => ({ id })),
      voiceCard: v => `<figure>${v.id}</figure>`,
    });
    assert.deepEqual(voiceRows.map(r => (r.innerHTML.match(/<figure>/g) || []).length), still ? [5, 4] : [10, 8]);
    assert.equal(voiceRows.every(r => r.innerHTML.includes('aria-hidden="true"')), !still);
    assert.ok(voiceCols.every(c => (c.innerHTML.match(/<figure>/g) || []).length === (still ? 3 : 6)));
  });
}
