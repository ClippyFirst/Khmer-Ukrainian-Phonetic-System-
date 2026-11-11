const JOTATED_VOWELS = {
  a: "я", "aː": "я", ɑ: "я", "ɑː": "я",
  e: "є", "eː": "є", ɛ: "є", "ɛː": "є",
  i: "ї", "iː": "ї",
  o: "йо", "oː": "йо", ɔ: "йо", "ɔː": "йо",
  u: "ю", "uː": "ю",
  ɨ: "йи", "ɨː": "йи",
};

export function mapIpa(ipa, practicalPolicy) {
  const segments = Object.keys(practicalPolicy.segments)
    .sort((a, b) => b.length - a.length);
  let rest = ipa.replace(/[ˈˌ]/gu, "");
  let value = "";
  let syllableStart = true;
  while (rest) {
    if (/\s/u.test(rest[0])) {
      value += rest[0];
      rest = rest.slice(1);
      syllableStart = true;
      continue;
    }
    if (rest[0] === "." || rest[0] === "·") {
      rest = rest.slice(1);
      syllableStart = true;
      continue;
    }
    const segment = segments.find((candidate) => rest.startsWith(candidate));
    if (!segment) return { value: null, unsupported: rest };
    if (syllableStart && segment === "j") {
      const afterJ = rest.slice(segment.length);
      const vowel = segments.find((candidate) => afterJ.startsWith(candidate));
      if (vowel && Object.hasOwn(JOTATED_VOWELS, vowel)) {
        value += JOTATED_VOWELS[vowel];
        rest = afterJ.slice(vowel.length);
        syllableStart = false;
        continue;
      }
    }
    value += practicalPolicy.segments[segment].default;
    rest = rest.slice(segment.length);
    syllableStart = false;
  }
  return { value, unsupported: null };
}
