const assert=require('node:assert/strict');
const {tokenizeIPA,sequenceFromIPA,validateSequence}=require('../dist/index.js');
const cases=[
 ['ˈt͡ʃiko',['t͡ʃ','i','k','o']],
 ['tʃa',['tʃ','a']],
 ['ã',['ã']],
 ['ˈkasa',['k','a','s','a']],
 ['la kasa',['l','a','word-boundary','k','a','s','a']],
 ['t͜ʃa',['t͜ʃ','a']],
 ['ˌd͡ʒa',['d͡ʒ','a']]
];
for(const [input,expected] of cases)assert.deepEqual(tokenizeIPA(input).map(t=>t.symbol),expected,input);
assert.equal(tokenizeIPA('ˈkasa')[0].stress,true);
assert.equal(tokenizeIPA('la kasa')[2].kind,'pause');
const s=sequenceFromIPA('ˈt͡ʃiko',{engine:'legacy-espeak-cli-ipa',version:'fixture',licenseStatus:'review-required'});
assert.equal(validateSequence(s),true);
assert.equal(validateSequence({...s,tokens:[{symbol:'a',kind:'phoneme',durationMs:-1}]}),false);
assert.throws(()=>sequenceFromIPA(' ',s.source));
console.log('PASS: 11 deterministic assertions; TS runtime requires no Python/eSpeak');
