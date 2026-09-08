const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync(require('node:path').join(__dirname, 'motion.js'), 'utf8');
for (const [system, saved, expected, control] of [[false,null,'on','hide'],[true,null,'off','show'],[true,'on','on','show'],[false,'off','off','show']]) {
  test(`system reduced=${system}, saved=${saved}`, () => {
    const dataset = {};
    runInNewContext(source, { matchMedia: () => ({matches:system}), history:{state:null},
      localStorage:{getItem:()=>saved}, document:{documentElement:{dataset}} });
    assert.equal(dataset.motion, expected); assert.equal(dataset.motionControl,control);
  });
}
test('visit preference survives blocked storage', () => {
  const dataset={};
  runInNewContext(source,{matchMedia:()=>({matches:true}),history:{state:{levxMotion:'on'}},
    localStorage:{getItem(){throw Error('blocked');}},document:{documentElement:{dataset}}});
  assert.equal(dataset.motion,'on');
});
