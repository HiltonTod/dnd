# To-do list

Tracked suggestions from reading the full corpus (ch. 1–85, including ch. 54) and the appendix. Nothing here has been
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

## 2. Chapter 55 was never written

Not a numbering skip — a session that never got written up. ~~Ch. 53~~ **written 22–23 Aug 2026** and
~~ch. 54~~ **written 24 Aug 2026**, both published under their session dates (14 and 28 April 2025).
Ch. 53 covers the end of White Plume Mountain, Tham's betrayal, Alustriel's rescue, and Neverember's
commission. Ch. 54 covers the breakfast briefing — the four victims named, the House of Knowledge
divinations, Hallix Mausoleum — and The Lady's second appearance, which is the campaign's central
exposition. Hallix is therefore **no longer missing**; it is introduced in ch. 54.

Still missing, per the appendix: the Gilded Glyph (magic shop, Maelis Varn) and the Fucking Duck
(dwarven jeweler). Ch. 56 still opens with "The adventurers leave The Gilded Glyph," a shop the
reader has never seen. Tod repointed the two shop entries from ch. 54 to ch. 55 in the same pass that
merged ch. 54, so the appendix is internally consistent.

- [ ] Decide for 55: write it, or leave it as a gap and fix the links to point elsewhere

**Ch. 55 was the party's first-ever magic shopping trip** and its consequences are already loose in
the prose. Full item list is in `characters.md` under "Gear bought off-page." Four items were bought
and paid for but have **never once appeared in a chapter**:

- [ ] **Mond — Draconic Sigil Tattoo** (2,000 gp). Free *shield* once/long rest, and a
      drop-to-1-HP-and-explode effect that has never fired on the page
- [ ] **Dolor — Signet Ring of Wyrmkind Favor** (4,000 gp). +2 Cha and advantage on Intimidation and
      Persuasion. He does a lot of talking to NPCs; this has never been visible in any of it
- [ ] **Grindlefoot — Collar of Breath and Blood** (4,500 gp). Deliberately re-specced from an amulet
      to a **collar so it stays on when he wild shapes** — a visual that should appear every
      transformation and never has
- [ ] **Grindlefoot — Seed Pouch of Old Barrows** (500 gp). Grows cover, healing herbs, or odd fruit
      overnight; refills each new moon. An unused story device, and a very Grindlefoot one
- [ ] **Bilwin — Ironbound Wardchain** (2,000 gp) is probably the "dwarf's chainmail" in ch. 66 and
      73, but is never named, and its once-a-day save-from-zero has never visibly triggered

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

- [x] ~~**Keyward: two spellings.**~~ **Resolved 24 Aug 2026 — Tod's call: Eldon, with an o.**
      Renamed across the corpus: ch. 59, 60, 61, 62, 62-ai, 63, and the appendix. Ch. 54 already had
      it right. `story-so-far.md` and `writing-voice.md` updated too. **Eldon Keyward is now the only
      spelling in the repo.**
- [ ] **Ch. 54 HTML comment**: "siutation" for "situation", in the cut Bilwin battle-hammer aside.
      Cosmetic — it does not render — but it is in the working notes if that aside is ever restored.
- [ ] **Ch. 54 has no `co-written-with-claude` tag.** If it was drafted with Claude it needs one per
      `CLAUDE.md`; if Tod wrote it unaided, no action. Its tags are `eve-of-ruin` and `neverwinter`
      only — note it also carries no `secret-learned` tag despite being the chapter where the party
      learns what the weapons did.

- [ ] "Cyndal" for Cindel, in the Low Elves membership list
- [ ] "Inda Malayui" (Characters) vs "Inda Malayuri" (Ships) — same person
- [ ] "The Guilded Glyph" → "Gilded" (in the Fucking Duck entry)
- [ ] Eldon Keyward described as "Male elven scholar" then "enlists the group to find **her**"
      (copy-paste from the Sarcelle / Indrina / Umberto entries, which share the sentence)
- [ ] "praticioners" → practitioners (Eyes of the Star entry)
- [ ] "proprieter" → proprietor (Boscoe); "penchance" → penchant (Dave Chevits)

### Missing and wrong chapter citations — the archmages

**The Sanctum cast are the most under-cited entries in the appendix.** All four NPCs appear in
chapters their entries don't list, and one entry cites a chapter its subject isn't in. Verified by
grepping the rendered prose of every chapter with HTML comments stripped, so passing mentions count
(per `appendix-guide.md` step 1) but working notes don't.

| Entry | Section | Appears in | Currently cited | **Add** | **Remove** |
|---|---|---|---|---|---|
| **Alustriel Silverhand** | Characters | 63, 64, 66, 67, 68, 74, 75 | 55, 63, 64, 67, 74, 75 | **66, 68** | — |
| **Tasha** | Characters | 64, 67, 68, 74, 75 | 64, 67, 74, 75 | **68** | — |
| **Mordenkainen** | Characters | 63, 64, 67, 68, 74, 84 | 63, 64, 67, 74, 75, 84 | **68** | **75** |
| **Malaina van Talstiv** | Characters | 67, 68, 74 | 67, 74 | **68** | — |
| **The Sanctum** | Shops, inns, & pubs | 64, 66, 67, 74, 75, 84 | 64, 74, 84 | **66, 67, 75** | — |

- [x] ~~**Alustriel Silverhand — add ch. 66 and 68.**~~  **Done** in the ch. 85 appendix pass.
       Ch. 66: her voice comes through the portal,
      *"Come now, let's not tarry in this unpleasant place."* Ch. 68: she breakfasts with the party
      and opens the portal to the Astral Plane.
- [x] ~~**Tasha — add ch. 68.**~~  **Done** in the ch. 85 appendix pass.
       She is named at the morning meal and is present when the archmages
      see the party off.
- [x] ~~**Mordenkainen — add ch. 68**~~  **Done** in the ch. 85 appendix pass.
      , where he is at the meal and the send-off.
- [x] ~~**Mordenkainen — remove ch. 75.**~~  **Done** in the ch. 85 appendix pass.
       He is not in that chapter. `grep -ci mordenkainen` on
      `_posts/2026-03-30-chapter-75.md` returns **0**. The archmage in ch. 75 is Tasha, with the
      potato-scrying scene, and she is already cited for it.
- [x] ~~**Malaina van Talstiv — add ch. 68.**~~  **Done** in the ch. 85 appendix pass.
       *"followed shortly by Malaina's silent entrance"*, and
      she is named again in the list of who accompanies the morning meal.
- [x] ~~**The Sanctum — add ch. 66, 67, and 75.**~~  **Done** in the ch. 85 appendix pass.
       Ch. 66 returns there through the portal, ch. 67 is
      the baths-and-dinner chapter set entirely inside it, ch. 75 opens with Grindlefoot wandering
      its halls.

**Done.** Ch. 85's own appendix pass added the three archmages, Landro, the Sanctum, Sigil and Ialos,
and created entries for the Grimoire of Gastronomy, the batter golem and the Sunburst Shield.

**Not part of this item:** Alustriel's ch. 55 citation is one of the seven links to unwritten
chapters, tracked in item 2. Leave it until that decision is made.

**While you're in these entries**, the descriptions are thin — Alustriel's reads "known for being
intelligent, wise, charismatic, and very beautiful," which is a stat block rather than a person,
and Tasha's doesn't mention that she is the one who will keep Vecna after the Chime of Exile, which
is her whole reason for being in the campaign. `npc-characters.md` has the material for both.

- [ ] Ch. 74's prose links the name *Mordenkainen* to **Alustriel's** wiki page. Copy-paste slip in
      the chapter, not the appendix, but it surfaced during the same pass.

### Missing entries

- [x] ~~**The Sunburst Shield has no appendix entry**~~  **Done** in the ch. 85 appendix pass.
      , and is now named in three chapters. Bilwin
      buys it in ch. 63 from an inebriated dwarf in a Bluelake market, and it is Hanseath's:
      *"The Bearded One drank a beer with it, sang a rousin' tune, and then called it the Sunburst
      Shield."* PR #93 named it in ch. 73 and ch. 78 as well, replacing the holy symbol that had
      crept into the drafted chapters. Belongs under **Objects**, immediately before Tempest Edge
      (nothing else in that section falls between S and T). Stated mechanics, for the sub-bullet: *"It can shine a light as bright
      as daylight once a day for ten minutes and the undead really don't like it."* Cite ch. 63, 73,
      and 78.

Same class as the paid-for-but-never-written items in section 2 — a thing that exists in the
fiction and is invisible in the reference. Worth a sweep for others: any item acquired on the page
that hasn't been named since.

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

- [x] ~~**Ch. 78 is missing `co-written-with-claude`.**~~ **Done** in PR #85 (commit `6be349e`).
      Chapters 78–83 now all carry the tag, so the drafted run is tagged consistently end to end.

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
