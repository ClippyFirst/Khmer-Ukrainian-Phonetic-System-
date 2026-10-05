const CONSONANTS = {
  "ក":"k","ខ":"kʰ","គ":"k","ឃ":"kʰ","ង":"ŋ","ច":"c","ឆ":"cʰ","ជ":"c","ឈ":"cʰ","ញ":"ɲ",
  "ដ":"ɗ","ឋ":"tʰ","ឌ":"ɗ","ឍ":"tʰ","ណ":"n","ត":"t","ថ":"tʰ","ទ":"t","ធ":"tʰ","ន":"n",
  "ប":"ɓ","ផ":"pʰ","ព":"p","ភ":"pʰ","ម":"m","យ":"j","រ":"r","ល":"l","វ":"ʋ","ស":"s","ហ":"h","ឡ":"l","អ":"ʔ"
};
const VOWELS = {"ិ":"i","ី":"iː","ឹ":"ɨ","ឺ":"ɨː","ុ":"u","ូ":"uː","េ":"e","ែ":"ɛː","ៃ":"əj","ោ":"ao","ៅ":"aw","ា":"aː","ួ":"uə","ៀ":"iə","ើ":"əə","ឿ":"ɨə","ឿ":"ɨə","ៃ":"əj"};
const BASE_VOWEL = {"ក":"ɑː","ខ":"ɑː","គ":"ɔː","ឃ":"ɔː","ច":"ɑː","ឆ":"ɑː","ជ":"ɔː","ឈ":"ɔː","ត":"ɑː","ថ":"ɑː","ទ":"ɔː","ធ":"ɔː","ប":"ɑː","ផ":"ɑː","ព":"ɔː","ភ":"ɔː","ម":"ɑː","យ":"ɔː","រ":"ɑː","ល":"ɑː","វ":"ɔː","ស":"ɑː","ហ":"ɔː","ឡ":"ɑː","អ":"ɑː"};
const UA = {"p":"п","pʰ":"п","b":"б","ɓ":"б","t":"т","tʰ":"т","d":"д","ɗ":"д","k":"к","kʰ":"к","c":"ч","cʰ":"ч","ɲ":"нь","ŋ":"нг","r":"р","l":"л","ʋ":"в","w":"в","j":"й","s":"с","h":"г","ʔ":"","m":"м","n":"н","i":"і","iː":"і","e":"е","eː":"е","ɛ":"е","ɛː":"е","ɨ":"и","ɨː":"и","a":"а","aː":"а","ɑ":"а","ɑː":"а","o":"о","oː":"о","u":"у","uː":"у","ə":"е","ɤ":"е","əj":"ей","iə":"іа","uə":"уа","ɨə":"ие","ao":"ау","aw":"ау"};
const EXAMPLES = {
  "ខ្មែរ": {ipa:"/kʰmae/", ua:"кмае", status:"PROPOSED", note:"IPA засвідчено; базова система нейтралізує аспірацію /kʰ/ → к. Це не усталена українська назва."},
  "ភ្នំពេញ": {ipa:"/pʰnum pɨɲ/", ua:"пнум пинь", status:"PROPOSED", note:"Фонетична форма засвідчена; практичний український результат є авторською пропозицією."}
};
const COENG="្";
const norm=s=>s.normalize("NFC");
const isKhmerConsonant=c=>Object.hasOwn(CONSONANTS,c);
function tokenize(text){
  const out=[]; let cur="";
  for(const c of norm(text)){
    if(/\s|[។៕,!?;:()[\]{}"“”«»]/u.test(c)){if(cur)out.push(cur),cur="";out.push(c);continue;}
    if(cur && isKhmerConsonant(c) && !cur.endsWith(COENG)){out.push(cur);cur=c;} else cur+=c;
  }
  if(cur)out.push(cur); return out;
}
function syllableIPA(raw){
  if(!raw || !isKhmerConsonant(raw[0])) return null;
  let i=0, base=raw[0], onset=CONSONANTS[base], subs=[];
  i=1;
  while(raw[i]===COENG && isKhmerConsonant(raw[i+1])){subs.push(CONSONANTS[raw[i+1]]);i+=2;}
  let vowel=null;
  for(;i<raw.length;i++){if(VOWELS[raw[i]]){vowel=VOWELS[raw[i]];break;}}
  if(!vowel) vowel=BASE_VOWEL[base];
  if(!vowel) return null;
  const onsetAll=onset+subs.join("");
  return onsetAll+vowel;
}
function ipaToUA(ipa){
  const tokens=["pʰ","tʰ","kʰ","cʰ","iː","uː","eː","ɛː","ɨː","aː","oː","ɑː","əj","iə","uə","ɨə","ao","aw","ŋ","ɲ","ʋ","ʔ","p","t","k","c","b","ɓ","d","ɗ","r","l","j","s","h","m","n","i","u","e","ɛ","ɨ","a","o","ɑ","ə","ɤ"];
  let rest=ipa,out="";
  while(rest){const t=tokens.find(x=>rest.startsWith(x));if(!t)return {value:null,unsupported:rest};out+=UA[t]??"";rest=rest.slice(t.length);}
  return {value:out,unsupported:null};
}
function convert(text,profile){
  const n=norm(text); if(!n.trim()) return null;
  if(EXAMPLES[n]){const x=EXAMPLES[n];return {...x,source:n,profile};}
  const units=tokenize(n); const ipaParts=[],uaParts=[],issues=[];
  for(const u of units){
    if(/\s|[។៕,!?;:()[\]{}"“”«»]/u.test(u)){ipaParts.push(u);uaParts.push(u);continue;}
    const ipa=syllableIPA(u);
    if(!ipa){issues.push(`«${u}» — точна фонетизація ще не встановлена.`);ipaParts.push("⟦NOT_ESTABLISHED⟧");uaParts.push("⟦НЕВСТАНОВЛЕНО⟧");continue;}
    const rendered=profile==="phnom_penh_colloquial"?ipa.replace(/([ptkbdc])r(?=[aeiouəɛɔɑɨɤ])/g,"$1ʰ"):ipa;
    const mapped=ipaToUA(rendered);
    if(!mapped.value){issues.push(`«${u}» — IPA ${rendered} містить непідтриманий сегмент «${mapped.unsupported}».`);uaParts.push("⟦НЕВСТАНОВЛЕНО⟧");}else{ipaParts.push("/"+rendered+"/");uaParts.push(mapped.value);}
  }
  return {source:n,ipa:ipaParts.join(" "),ua:uaParts.join(""),status:issues.length?"EVIDENCE_LIMITED":"PROPOSED",note:issues.length?issues.join(" "):"Графемну структуру розпізнано; фонетичні значення, які не покриває повна матриця, позначаються явно.",profile};
}
const $=id=>document.getElementById(id);
const source=$("source"),results=$("results"),empty=$("empty"),issue=$("issue"),live=$("live");
function render(){
  $("count").textContent=[...source.value].length+" символів";
  const data=convert(source.value,$("profile").value);
  if(!data){results.hidden=true;issue.hidden=true;empty.hidden=false;return;}
  empty.hidden=true;results.hidden=false;
  $("source-result").textContent=data.source;$("ipa-result").textContent=data.ipa;$("ua-result").textContent=data.ua;
  $("status").textContent=data.status.replaceAll("_"," ");
  $("details").textContent=data.note;
  issue.hidden=!data.note || data.status==="PROPOSED";
  if(!issue.hidden)$("issue-text").textContent=data.note;
  live.textContent="Результат оновлено";
}
source.addEventListener("input",render);$("profile").addEventListener("change",render);
$("example").addEventListener("click",()=>{source.value="ខ្មែរ";render();source.focus();});
$("clear").addEventListener("click",()=>{source.value="";render();source.focus();});
document.querySelectorAll("[data-copy]").forEach(b=>b.addEventListener("click",async()=>{const el=$(b.dataset.copy);await navigator.clipboard.writeText(el.textContent);const old=b.textContent;b.textContent="Скопійовано";setTimeout(()=>b.textContent=old,900);}));
