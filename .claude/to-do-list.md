# To-do list

Tracked suggestions from reading the full corpus (ch. 1–83) and the appendix. Nothing here has been
acted on — these are proposals for Tod to accept, reject, or reorder. Check items off in place.

Grouped by size, biggest commitment first.

---

## 1. Convert list-form combat to prose (19 chapters)

The largest item. These chapters still render turn-by-turn bulleted combat with damage numbers on
the page, under a visible `## Fight choreography` heading. The intent is that all combat is prose.

- [ ] ch. 6
- [ ] ch. 7
- [ ] ch. 8
- [ ] ch. 9
- [ ] ch. 10 — heading reads `## Encounter choreography` (the Vera rescue, a stealth set piece)
- [ ] ch. 12
- [ ] **ch. 13 — biggest job.** Twelve numbered rounds of the Battle of Wayside, no prose at all
- [ ] ch. 14
- [ ] ch. 17
- [ ] ch. 21
- [ ] ch. 25
- [ ] ch. 27
- [ ] ch. 29
- [ ] ch. 30 — heading reads `## Storm choreography`; a non-combat skill challenge, eight rounds
- [ ] ch. 31
- [ ] ch. 33
- [ ] ch. 35
- [ ] ch. 36
- [ ] ch. 38 — partial; already has prose *and* the list. Just needs the comment cleanup
- [ ] ch. 1 — combat is already prose; only the `## Fight choreography` heading needs removing

**Model to follow:** ch. 38 carries both forms in one file. The comment says "Green grung 4 -
Grapples Dolor and rubs his hands over Dolor's neck"; the prose says the creature "lands on Dolor's
back, grabs hold tightly of his neck, and secretes a slimy substance onto his skin," and later
Dolor wonders where a naked frog was keeping a knife. Keep the list in an HTML comment as the
working record, write prose from it, drop the numbers.

**Also worth doing while in there:** chapters 2, 3, 4, 39, and 43 have prose already but retain
`<!-- Step-by-step -->` comment blocks. Those are fine to leave — they're working notes, and
CLAUDE.md says to preserve HTML comments.

---

## 2. Chapters 53, 54, 55 were never written

Not a numbering skip — three sessions that never got written up. The appendix documents their
content and links to them, so **seven appendix links are 404s on the live site**, and ch. 56 opens
with "The adventurers leave The Gilded Glyph," a shop the reader has never seen.

What happened in them, per the appendix: the arrival in Neverwinter, the Gilded Glyph (magic shop,
Maelis Varn), the Fucking Duck (dwarven jeweler), Hallix Mausoleum, and first contact with
Alustriel Silverhand.

- [ ] Decide: write them, or renumber, or leave them as a gap and fix the links to point elsewhere

---

## 3. Appendix corrections

**Do not fix silently — these are content decisions.** Listed roughly by how much damage they'd do
if a future chapter trusted them.

### Factual

- [ ] **Eyes of the Star and Hand of the Wand have their descriptions swapped.** Ch. 5 is explicit:
      the Hands of the Wand track *magic users* and are magic users themselves; the Eyes of the Star
      monitor *religious and faith-based* groups. The appendix says the reverse for both. The names
      side with ch. 5 — wand, arcane. This is load-bearing worldbuilding.
- [ ] **"Everwinter" should be "Evernight"** (2 places: the city entry and the Shadowfell entry).
      Ch. 59, 60, and 63 all say Evernight, as does ch. 59's tag. Evernight is also the canonical
      Forgotten Realms name for Neverwinter's Shadowfell mirror.
- [ ] **The Davanor entry is stale.** Still reads "Unknown gender and species… person of interest in
      Torp's disappearance," which ch. 28 resolved — Davanor *is* Torp. The two remain separate
      entries in separate sections (Torp under Characters, Davanor under Foes). Merge, cross-
      reference, or leave Davanor as a deliberate in-world stub.
- [ ] **Cindel:** "half-elven" in the appendix, "elf" every time she appears in ch. 1–4. Pick one.

### Open markers left in the file

- [ ] Indrina Lamsensettle — `[UPDATE - ch. ??]`
- [ ] Temple of Aish — `TODO - UPDATE Gustaf's map of the temple`

### Typos and inconsistencies

- [ ] "Cyndal" for Cindel, in the Low Elves membership list
- [ ] "Inda Malayui" (Characters) vs "Inda Malayuri" (Ships) — same person
- [ ] "The Guilded Glyph" → "Gilded" (in the Fucking Duck entry)
- [ ] Elden Keyward described as "Male elven scholar" then "enlists the group to find **her**"
      (copy-paste from the Sarcelle / Indrina / Umberto entries, which share the sentence)
- [ ] "praticioners" → practitioners (Eyes of the Star entry)
- [ ] "proprieter" → proprietor (Boscoe); "penchance" → penchant (Dave Chevits)

### Structural

- [ ] 15 entries carry no chapter citation while the rest do: Elar, Herbert, Lyra Swiftarrow, Preva,
      Ro'qu-ell-a, Vera, Gruumsh, Preva's Flower Shop, Lamayum River, Eritz, Mirganor, Olam, Quiet
      Valley, Unmarked Territories, Wayside
- [ ] Dolindar Family is filed under **Characters** but is a family/group — belongs under Groups
- [ ] Davanor, K'ren, Chuck, and Squiggy are filed under **Foes, monsters, & creatures** but are
      people. Defensible for antagonists; inconsistent with Cabanna and Magnus being under Characters

---

## 4. Proofreading across chapters

Roughly 48 recurring misspellings in ch. 60–77 alone, and the same pattern earlier.

- [ ] **`halfing` for `halfling`** — 11 occurrences, and spellcheck won't flag it. Highest value fix
- [ ] Others that recur: `concious`, `acquiesence`, `irridescent`, `death throws` (for "throes"),
      `occured`, `catastrophy`, `posessions`, `accomodations`, `demeaner`, `respit`
- [ ] **Nyx's surname is spelled two ways.** Ch. 39's prose says "Whisperfang" (4×); its own guest
      credit and ch. 41–42 say "Whiskerfang." Whiskerfang is the one that stuck
- [ ] A general spellcheck pass before publishing is the single cheapest quality improvement
      available anywhere in this list

---

## 5. Tags and metadata

- [ ] **Ch. 78 is missing `co-written-with-claude`.** It was the first Claude-drafted chapter — its
      own trailing comment says so — but only 79–83 carry the tag. Its current tags are
      `eve-of-ruin`, `fight`, `guest-player`, `landro`, `mournland`

---

## 6. Craft notes (optional, not defects)

Observations from the read that are worth considering but are nobody's bug.

- [ ] **The repeated map ending.** Chapters 45, 46, 48, 49, 50, 51, and 52 all close on the same
      Gustaf map image with an identical caption — seven of the eight chapters in that span. The
      framing around each one varies nicely; only the final beat repeats
- [ ] **Chapter openings.** 28% of chapters (22 of 80) open with a participial recap phrase
      ("Having defeated…", "After vanquishing…"). Effective, but better than one in four
- [ ] **The round-robin has gone missing.** Giving every companion an interior beat in sequence is
      the signature non-combat structure (ch. 42, 63, 67, 68, 76). Chapters 78–83 contain none
- [ ] **Dialogue rate.** Ch. 78–83 run ~5% spoken words against a historical ~24%. Six consecutive
      dungeon-crawl chapters with no talking chapter to reset is the anomaly, not any one chapter
- [ ] **The pun/parody register is dormant.** Food Alley (ch. 19–21) is a whole comic mode —
      Eclairvoyant's, The Fizz Hutt, Waffle Wizards — that hasn't been used since Elsemar
