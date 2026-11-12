// Orthographic rendering of the existing Khmer-to-Latin package output.
// The upstream package explicitly drops BGN/PCGN diacritics, so this adapter is
// PROVISIONAL and cannot reconstruct contextual vowel alternatives lost upstream.
const MAP = Object.freeze({
  chh:"ч'", kh:"к'", th:"т'", ph:"п'", nh:"нь", ng:"нг", ch:"ч",
  aoh:"аог", oah:"оаг", eah:"еаг", ah:"аг", oh:"ог", uh:"уг", eh:"ег",
  eang:"еанг", ang:"анг", aeu:"аеу", eu:"еу", ao:"ао", ou:"оу", au:"ау",
  ae:"ае", ai:"ай", ey:"ей", ie:"іє", oea:"иа", roe:"ри", loe:"ли", oe:"и",
  uo:"уо", om:"ом", oam:"оам", um:"ум", am:"ам", ei:"ей", a:"а", e:"е", i:"і", o:"о", u:"у",
  b:"б", d:"д", k:"к", l:"л", m:"м", n:"н", p:"п", r:"р", s:"с", t:"т", v:"в", y:"й", h:"г",
  "’":"ʼ", "'":"ʼ",
  c:null, f:null, g:null, j:null, q:null, w:null, x:null, z:null,
});
const KEYS=Object.keys(MAP).sort((a,b)=>b.length-a.length);
const isKhmer=char=>{const cp=char.codePointAt(0);return (cp>=0x1780&&cp<=0x17ff)||(cp>=0x19e0&&cp<=0x19ff);};

function renderLatinWord(value){
  let output="",unsupported=0,mapped=0;
  for(let i=0;i<value.length;){
    const rest=value.slice(i);
    const key=KEYS.find(candidate=>rest.toLowerCase().startsWith(candidate));
    if(!key){
      const char=String.fromCodePoint(value.codePointAt(i));
      if(/[A-Za-z]/u.test(char)){output+="⟦"+char+"⟧";unsupported+=1;}
      else output+=char;
      i+=char.length;continue;
    }
    const source=value.slice(i,i+key.length),target=MAP[key];
    if(target===null){output+="⟦"+source+"⟧";unsupported+=1;}
    else{
      const cased=/^[A-Z]/u.test(source)?target[0].toLocaleUpperCase("uk")+target.slice(1):target;
      output+=cased;mapped+=1;
    }
    i+=key.length;
  }
  return {text:output,mapped,unsupported};
}

export function renderKhmerRomanizationText(source,romanizer){
  const chars=[...String(source??"").normalize("NFC")];
  let output="",mapped=0,unsupported=0,hasKhmer=false;
  for(let i=0;i<chars.length;){
    if(!isKhmer(chars[i])){output+=chars[i];i+=1;continue;}
    hasKhmer=true;let run="";
    while(i<chars.length&&isKhmer(chars[i])){run+=chars[i];i+=1;}
    const latin=romanizer(run);
    const rendered=renderLatinWord(latin);
    output+=rendered.text;mapped+=rendered.mapped;unsupported+=rendered.unsupported;
  }
  return {
    text:output,
    status:!hasKhmer?"PASSTHROUGH":unsupported?"PARTIAL":"PROVISIONAL",
    mapped,unsupported,
    profile:"BGN/PCGN-derived ASCII (diacritics omitted upstream)",
  };
}

export { renderLatinWord };
