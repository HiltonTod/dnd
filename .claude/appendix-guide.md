# Appendix guide

How to update `_posts/2023-01-23-appendix.md` when a chapter is written. The appendix is the
campaign's reference of record — who, what, where — and it goes stale silently, because nothing
about writing a chapter forces you to open it.

**Do this pass after the chapter file is finished and before opening the PR.** It is part of
writing a chapter, not a separate chore.

Companion files: `writing-voice.md` (how to write), `characters.md` (the party),
`npc-characters.md` (how recurring NPCs sound), `story-so-far.md` (what happened),
`to-do-list.md` (tracked fixes).

## The pass

1. **List every proper noun in the new chapter** — people, constructs, places, items, factions,
   secrets. Include ones that only get a passing mention.
2. **For each, grep the appendix.** `grep -n -i "name" _posts/2023-01-23-appendix.md`
3. **Entry exists → append the chapter link** to its citation list. This is most of the work and
   it is nearly always right; an entry that stops citing chapters looks abandoned.
4. **No entry → decide.** Add one if the thing is named, recurs, or is load-bearing for a thread.
   Skip walk-ons and scenery. A named NPC who speaks almost always earns an entry. Keep it to one or
   two sentences — see *An entry says what a thing is* below.
5. **Ask whether anything changed category** — see below. This is the one that gets missed.
6. **Check the Secrets section** if the chapter learned, resolved, or spent a secret.

## An entry says what a thing *is*, not what happened to it

**The most common mistake in this pass, and the easiest one to make while the chapter is fresh.**
The appendix is an index. What happened belongs in `story-so-far.md`; how somebody sounds belongs in
`npc-characters.md`; the entry here is the short, flat statement of what the thing is, plus its
chapter links.

Every entry Tod cut from the chapter 85 pass was an entry that had drifted into narrative:

| Written | Should have been |
|---|---|
| "It has baths, guest rooms, a library, a solarium, and a kitchen the companions never find until ch. 85" | *(nothing — The Sanctum's existing description was fine)* |
| "The pilot's helmet taken from Landro is left with them on the way out of Mournland" | *(nothing — that is a plot event, and it lives in `story-so-far.md`)* |
| The Grimoire's five ingredients and the order Dolor deduced | *(nothing — the puzzle and its solution are the chapter's, not the index's)* |
| "The Sanctum is her home and she is the one who opens and closes every portal. Unfailingly composed." | *(nothing — that is characterisation, and it lives in `npc-characters.md`)* |

**So: when an existing entry is already accurate, the pass adds a chapter link and nothing else.**
Resist improving the description while you are in there. If the description is genuinely wrong or
stale, that is a content decision — track it in `to-do-list.md` rather than rewriting it in passing,
the same as the five known-wrong entries listed under *Don't fix silently*.

**New entries get one or two sentences.** Look at what is already there and match its register:

> **Batter golem** - A humanoid creature of pale golden batter that rises out of the mixing cauldron
> when a legendary confection is prepared.

Mechanics are the one thing that earns a sub-bullet, because the appendix is where the party's item
powers are recorded — see Tempest Edge, Whelm, and the Sunburst Shield. Plot is never a sub-bullet.

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
k=lambda x: re.sub(r'^(the|a|an) ','',re.sub(r'^\[','',x).lower())
print([(a,b) for a,b in zip(n,n[1:]) if k(a)>k(b)] or 'ordered')
"
```

Names sort past a leading `The` — `The Sanctum` sits under S, `The Grimoire of Gastronomy` under G.

Known pre-existing disorder, all of it fine to leave: `Thistlewick Brandlestrum` before `Tella` in
Characters; `Grinder's Mill` before `Gilded Glyph` and `Scribbles & Nibs` before `The Fizz Hutt` in
Shops; `Other Trail` before `The Broken Heart` in Landmarks.

## Don't fix silently

`writing-voice.md` lists four appendix entries known to be wrong or stale — the swapped
Eyes of the Star / Hand of the Wand descriptions, "Everwinter" for "Evernight", the Davanor entry,
and the Cindel species. (The seven links to unwritten chapters 53–55 are no longer an issue — all
three chapters were written in August 2026 and the links resolve.) Those are content decisions
tracked in `to-do-list.md`, not drive-by corrections. Fixing an obviously broken *link* while
you're in the file is fine; rewriting worldbuilding is not.
