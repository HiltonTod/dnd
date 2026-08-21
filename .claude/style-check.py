#!/usr/bin/env python3
"""Measure a chapter draft against Tod's voice in chapters 1-77.

    python3 .claude/style-check.py path/to/draft.md        # from the repo root

Reports the structural metrics in writing-voice.md under "Structure — the four things
that give a draft away", plus the contraction check. Baselines are computed live from
_posts/, so they stay true as the corpus grows.
"""
import re, sys, glob, statistics as st

DIALOGUE_VERBS = r'(?:says|asks|responds|replies|exclaims|adds|offers|explains|observes|notes|agrees|tells|continues)'

def clean(t):
    t = re.sub(r'^---\n.*?\n---\n', '', t, flags=re.S)   # front matter
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)         # HTML comments (working notes)
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', t)           # images
    return re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)    # links -> label

def words(s):  return re.findall(r"[A-Za-z][A-Za-z'’-]*", s)
def sents(s):  return [x for x in re.split(r'(?<=[.!?])\s+', re.sub(r'[ \t]+', ' ', s)) if words(x)]

def paras(t):
    return [p.strip() for p in re.split(r'\n\s*\n', t)
            if p.strip() and p.strip() != '---' and not p.strip().startswith('#')]

FRONTED = re.compile(
    r'^(?:[A-Z][a-z]+ing\b|Having\b|Seeing\b|Knowing\b|Standing\b|Noting\b|Realizing\b|Hearing\b'
    r'|Looking\b|Turning\b|Reaching\b|Holding\b|Moving\b|Walking\b|Taking\b|Feeling\b|Wondering\b'
    r'|Presuming\b|Surprised\b|Unable\b|Freed\b|With [a-z]+[^,]{0,40},|After [^,]{0,40},'
    r'|Before [^,]{0,40},|From [a-z][^,]{0,40},)[^.]{0,80},')

def measure(files):
    t = "\n\n".join(clean(open(f).read()) for f in files)
    P = paras(t)
    narr_p = [p for p in P if not p.lstrip().startswith('"')]
    all_s  = sents(re.sub(r'\n+', ' ', t))
    narr   = re.sub(r'"[^"]*"', ' ', t)                    # narration = outside quotes
    narr_s = sents(re.sub(r'\n+', ' ', narr))
    nsl    = [len(words(s)) for s in narr_s]
    npl    = [len(words(p)) for p in narr_p]
    turns  = [len(words(m)) for m in re.findall(r'"([^"]*)"', t) if words(m)]
    one    = sum(1 for p in narr_p if len(sents(p)) == 1)
    nw     = len(words(narr))
    contr  = len(re.findall(r"\b\w+['’](s|t|re|ve|ll|d|m)\b", narr))
    expand = sum(len(re.findall(r'\b' + f + r'\b', narr, re.I)) for f in
                 ['it is','does not','that is','they are','there is','he is','is not',
                  'are not','cannot','did not'])
    return {
        'words'        : len(words(t)),
        'fronted/100'  : 100 * sum(1 for s in all_s if FRONTED.match(s)) / max(len(all_s), 1),
        'para mean'    : st.mean(npl), 'para med': st.median(npl),
        '1-sent para%' : 100 * one / max(len(narr_p), 1),
        'sent mean'    : st.mean(nsl), 'sent med': st.median(nsl),
        'sent <=6w%'   : 100 * sum(1 for x in nsl if x <= 6) / len(nsl),
        'speech mean'  : st.mean(turns) if turns else 0,
        'collective/1k': 1000 * len(re.findall(r'\b(the companions|the group|the adventurers|the party)\b', t, re.I)) / max(len(words(t)), 1),
        'lead-in tags' : len(re.findall(r'\b\w+ ' + DIALOGUE_VERBS + r'[,:]\s*"', t, re.I)),
        'trailing tags': len(re.findall(r'"[^"]*,"\s+(?:the\s+\w+\s+)?\w+ ' + DIALOGUE_VERBS + r'\b', t, re.I)),
        'contract/1k'  : 1000 * contr / max(nw, 1),
        'expanded/10k' : 10000 * expand / max(nw, 1),
    }

def corpus(lo, hi):
    out = []
    for n in range(lo, hi + 1):
        out += [f for f in glob.glob('_posts/*chapter-%d.md' % n) if '-ai' not in f]
    return out

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    base = corpus(56, 77)
    if not base:
        sys.exit("No _posts/ found — run this from the repo root.")
    tod, draft = measure(base), measure([sys.argv[1]])
    print("%-16s %>10s %>10s" .replace('>','') % ('metric', 'you 56-77', 'draft'))
    print("-" * 40)
    for k in tod:
        a, b = tod[k], draft[k]
        fmt = "%-16s %10.1f %10.1f" if isinstance(a, float) else "%-16s %10d %10d"
        print(fmt % (k, a, b))
    print("\nTargets: fronted/100 ~9.7 | para mean ~53 | 1-sent para% ~19 | sent mean ~17"
          "\n         sent <=6w% ~9 | contract/1k ~17 (never below 12) | expanded/10k <15")
