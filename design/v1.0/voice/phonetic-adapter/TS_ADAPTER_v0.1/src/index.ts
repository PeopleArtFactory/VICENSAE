/** VICENSAE VOICE phonetic adapter, TS-only runtime; schema 0.1 compatible. */
export type Token = {symbol:string; kind:'phoneme'|'pause'|'unknown'; origin?:string; stress?:boolean; durationMs?:number};
export type Sequence = {
 schema:'vaes.phoneme-sequence/0.1'; language:'es';
 source:{engine:string;version:string;licenseStatus:'review-required'|'verified'};
 tokens:Token[];
};
const affricates=['t͡ʃ','d͡ʒ','tʃ','dʒ','t͜ʃ','d͜ʒ'];
const marks=/\p{M}/u;
const letters=/\p{L}/u;
export function tokenizeIPA(raw:string):Token[] {
 const out:Token[]=[];
 const words=raw.trim().split(/\s+/u).filter(Boolean);
 words.forEach((word,wi)=>{
  if(wi)out.push({symbol:'word-boundary',kind:'pause',origin:'ipa-whitespace;duration-unknown'});
  let pending:'primary'|'secondary'|null=null;
  const chars=Array.from(word);
  for(let i=0;i<chars.length;){
   const c=chars[i];
   if(c==='ˈ'||c==='ˌ'){pending=c==='ˈ'?'primary':'secondary';i++;continue;}
   if(c==='‿'){out.push({symbol:c,kind:'unknown',origin:'ipa-link-marker'});i++;continue;}
   let symbol:string;
   const match=affricates.find(a=>word.slice(chars.slice(0,i).join('').length).startsWith(a));
   if(match){symbol=match;i+=Array.from(match).length;}
   else {symbol=c;i++;while(i<chars.length&&marks.test(chars[i]))symbol+=chars[i++];}
   const kind=letters.test(Array.from(symbol)[0])?'phoneme':'unknown';
   const token:Token={symbol,kind,origin:'ipa-longest-match-provisional'};
   if(pending&&kind==='phoneme'){token.stress=true;token.origin+=';'+pending+'-stress';pending=null;}
   out.push(token);
  }
 });
 return out;
}
export function sequenceFromIPA(raw:string, source:Sequence['source']):Sequence {
 if(!raw.trim())throw new Error('Empty IPA');
 return {schema:'vaes.phoneme-sequence/0.1',language:'es',source,tokens:tokenizeIPA(raw)};
}
export function validateSequence(input:unknown):input is Sequence {
 if(!input||typeof input!=='object')return false;
 const x=input as Record<string,unknown>;
 if(x.schema!=='vaes.phoneme-sequence/0.1'||x.language!=='es'||!Array.isArray(x.tokens))return false;
 const s=x.source as Record<string,unknown>|undefined;
 if(!s||typeof s.engine!=='string'||typeof s.version!=='string'||!['review-required','verified'].includes(String(s.licenseStatus)))return false;
 return x.tokens.every((t:unknown)=>{
  if(!t||typeof t!=='object')return false;
  const z=t as Record<string,unknown>;
  return typeof z.symbol==='string'&&z.symbol.length>0&&['phoneme','pause','unknown'].includes(String(z.kind))&&
   (z.origin===undefined||typeof z.origin==='string')&&
   (z.stress===undefined||typeof z.stress==='boolean')&&
   (z.durationMs===undefined||(typeof z.durationMs==='number'&&Number.isFinite(z.durationMs)&&z.durationMs>=0));
 });
}
