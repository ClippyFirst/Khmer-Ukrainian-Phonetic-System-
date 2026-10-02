import argparse, json
from .parser import analyze

def main():
    p=argparse.ArgumentParser(prog="khmer-ua")
    sub=p.add_subparsers(dest="command",required=True)
    for name in ("analyze","syllables","ipa","transliterate","explain"):
        q=sub.add_parser(name); q.add_argument("text")
    for name in ("validate","generate","benchmark","coverage"):
        sub.add_parser(name)
    a=p.parse_args()
    if a.command in {"analyze","syllables","ipa","transliterate","explain"}:
        r=analyze(a.text)
        if a.command=="syllables": print(json.dumps(r.syllables,ensure_ascii=False,indent=2))
        elif a.command=="ipa": print(r.ipa or "NOT ESTABLISHED")
        else: print(json.dumps(r.__dict__,ensure_ascii=False,indent=2,default=str))
    else:
        print(json.dumps({"command":a.command,"status":"IMPLEMENTATION_REQUIRED","reason":"No empirical corpus/complete generators are claimed yet."},indent=2))

if __name__=="__main__": main()
