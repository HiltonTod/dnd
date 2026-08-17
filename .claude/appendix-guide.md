# Appendix guide

How to update `_posts/2023-01-23-appendix.md` when a chapter is written. The appendix is the
campaign's reference of record — who, what, where — and it goes stale silently, because nothing
about writing a chapter forces you to open it.

**Do this pass after the chapter file is finished and before opening the PR.** It is part of
writing a chapter, not a separate chore.

Companion files: `writing-voice.md` (how to write), `characters.md` (who they are),
`story-so-far.md` (what happened), `to-do-list.md` (tracked fixes).

## The pass

1. **List every proper noun in the new chapter** — people, constructs, places, items, factions,
   secrets. Include ones that only get a passing mention.
2. **For each, grep the appendix.** `grep -n -i "name" _posts/2023-01-23-appendix.md`
3. **Entry exists → append the chapter link** to its citation list. This is most of the work and
   it is nearly always right; an entry that stops citing chapters looks abandoned.
4. **No entry → decide.** Add one if the thing is named, recurs, or is load-bearing for a thread.
   Skip walk-ons and scenery. A named NPC who speaks almost always earns an entry.
5. **Ask whether anything changed category** — see below. This is the one that gets missed.
6. **Check the Secrets section** if the chapter learned, resolved, or spent a secret.

## Changed category — the trap

The appendix files by *what a thing is*, and chapters can change that. The check is: **did this
chapter reveal that an entry is filed under the wrong heading, or that it is now two things?**

The worked example is **Landro**. It sat under **Objects** as "a monstrous colossus located in the
Mournland" from ch. 77 to 83. Chapter 84 made that wrong twice: the colossus is destroyed, and
Landro was never the colossus to begin with — *"The construct is not me either."* It became two
entries, a **Character** (the mind, which joins the party) and an **Object** renamed
**Landro (the colossus)** recording the destruction and pointing at the character.

`to-do-list.md` tracks the same class of problem elsewhere: Davanor, K'ren, Chuck and Squiggy are
people filed under *Foes, monsters, & creatures*, and Dolindar Family is a group filed under
*Characters*. Don't add to that pile.

## Sections, in file order

`History` (Battles, Events) · `People` (Adventurers, Characters, Deities, Foes/monsters/creatures,
Groups) · `Places` (Ships, Shops/inns/pubs, Landmarks/roads/trails, Towns/villages/cities) ·
`Things` (Objects, Plants, Secrets)

## Format rules

Match the surrounding entries exactly. The ones that actually bite:

- Bullet is `*` followed by **three spaces**. Continuation lines indent **four spaces**.
- **Alphabetical by first name** within a section — Landro sits between Kycera and Lyra Swiftarrow,
  Filch between Figaro and Flo.
- Citations are `[[ch. N](/dnd/campaign/chapter-N/)]`, comma-separated, wrapped across lines.
  **The trailing slash is mandatory** — without it the link 404s on the live site. Glaive's ch. 80
  link was missing one for three chapters.
- Sub-facts (item powers, a spent secret) are indented bullets under the parent entry.
- Species, classes, and game terms are linked on first use, same targets as the chapters use.

## Secrets

The Secrets section records what the party has taken via the Vecna link. A secret has a life
beyond being learned: it can be **resolved** in the story and later **spent** for a mechanical
benefit. Record both, as indented bullets, and say how. `Mercy's Secret` is the model — learned in
ch. 76, resolved in ch. 78, spent in ch. 84 to give Landro a memory.

## Before committing

```bash
f=_posts/2023-01-23-appendix.md

# every chapter link must end in a slash — this must print nothing
grep -o "](/dnd/campaign/chapter-[0-9]*[^)]*)" $f | grep -v "/)$" | sort -u

# alphabetical order within a section (edit the section name)
python3 -c "
import re; L=open('$f').read().split('\n')
s=next(i for i,l in enumerate(L) if l.startswith('## Characters'))
e=next(i for i,l in enumerate(L) if i>s and l.startswith('## '))
n=[re.match(r'\*   \*\*(.+?)\*\*',l).group(1) for l in L[s:e] if re.match(r'\*   \*\*',l)]
print([(a,b) for a,b in zip(n,n[1:]) if a.lower().lstrip('[')>b.lower().lstrip('[')] or 'ordered')
"
```

Known pre-existing disorder: `Thistlewick Brandlestrum` before `Tella` in Characters. Leave it.

## Don't fix silently

`writing-voice.md` lists five appendix entries known to be wrong or stale — the swapped
Eyes of the Star / Hand of the Wand descriptions, "Everwinter" for "Evernight", the Davanor entry,
the Cindel species, and the seven links to unwritten chapters 53–55. Those are content decisions
tracked in `to-do-list.md`, not drive-by corrections. Fixing an obviously broken *link* while
you're in the file is fine; rewriting worldbuilding is not.
