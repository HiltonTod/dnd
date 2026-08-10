# Writing voice

Derived by reading chapters 60–77, written by Tod without assistance, and chapters 78–83,
co-written by Tod and Claude. Supporting measurements draw on the full corpus, chapters 1–83.

One exception to "written by Tod": **chapter 26 carries the comment `Originally written by Liam and
edited by Tod`**, and Liam's raw session notes are preserved below it. It is the only chapter in
1–77 with another author's hand in it, and it reads slightly differently — more past tense, more
summary — which is worth knowing before treating it as a style sample.

Quotes below are verbatim from the repo. This file exists so the voice lives in the repo rather
than in any one tool's memory.

**Reading coverage.** All 83 chapters have now been read in full (53–55 do not exist). Everything
below is both measured and read.

## The workflow that produced these

From your own note in `2026-05-04-chapter-78.md`:

> This chapter was drafted by Claude. I had Claude review the 77 chapters I had written to
> understand the storylines, characters, and my writing style. I dictated my notes into a Google
> Doc, pasted that into Claude, and had it write a first draft, then a second. I manually edited
> the final draft, putting my own touches and style on it.

Two drafts, then your edit. The second draft matters — the first one gets the events down, the
second one finds the beats. Don't hand over a first draft as though it's finished.

## What changed at chapter 78

Not a clean break. Chapter 78 is a hinge, but only some of what shifted there is real, and almost
none of it is an improvement to copy wholesale.

**Genuine reversals — these are what to fix:**

| | Ch. 61–77 | Ch. 78–83 |
|---|---|---|
| Spoken words as % of prose | 24.3% | **5.0%** |
| Round-robin interior sequences | ch. 63, 67, 68, 76 | **none** |
| Chapters with little or no combat | ch. 63, 74, 75 | **none** — all six are dungeon crawl |
| Words per chapter | 2,608 | 2,045 |
| Spaced em dash ` — ` | 0 in 151k words | 27.7 per 10k |

Each of these runs *against* your own trajectory. Chapter length had been growing (r = +0.54) and
dialogue rising (r = +0.18) across the whole campaign.

**Continuations, not breaks** — you were already heading here, so there is nothing to undo:

- Sentence length 16.3 → 14.5 words, extending a decline since chapter 1 (r = −0.55)
- Paragraph length 52.1 → 39.9 words, extending a decline since chapter 1 (r = −0.47)
- `-ly` adverbs 18.0 → 13.9 per 1,000 words
- Hedging verbs (`begins to`, `seems to`, `appears to be`) cut to near zero — a real gain

**Overstated.** Combat compression is real but modest: 578 words per round in ch. 61–77 versus 415
in 78–83, a 28% reduction rather than a categorical change. Chapter 78 itself runs 744 words per
round, the densest in the recent run.

**Not stylistic at all.** The hard-wrapping change (your lines wrap near 120 characters; the drafted
files run one long line per paragraph) is an artifact of pasting out of a chat window.

**Wrong in an earlier draft of this file, corrected here:** emotional beats were *not* previously
summarized. Chapters 63, 66, 67, 68, and 74 give them more room than anything in 78–83 — five bath
scenes, a childhood flashback with Torp, Grindlefoot's whole farming backstory. What 78–83 has is
one very good scene (Mercy and Filch) and no round-robins at all.

## Your style was already moving

Measured across all 80 chapters, two of the four shifts at ch. 78 are not a break at all — they are
your own three-year trajectory, accelerated:

| Chapters | words | dialogue % | sentence len | paragraph words |
|---|---|---|---|---|
| 1–20 | 1,653 | 14.7% | 19.5 | 77.5 |
| 21–40 | 1,619 | 27.6% | 18.5 | 62.5 |
| 41–60 | 2,338 | 18.8% | 17.3 | 48.5 |
| 61–77 | 2,608 | 24.2% | 16.3 | 52.1 |
| 78–83 | 2,045 | **5.2%** | 14.6 | 39.9 |

Sentence length has fallen steadily since chapter 1 (r = −0.55) and so has paragraph length
(r = −0.47). The drafted chapters continue both. But chapter length had been *growing* (r = +0.54)
and dialogue *rising* (r = +0.18) — and 78–83 reverse both.

The longest run of ≤10%-dialogue chapters anywhere before this was **4**, back at chapter 10. The
drafted run is **6 consecutive**. That is the anomaly.

**But dialogue rate tracks mode, not just era.** Reading the dungeon-crawl chapters confirms it:
ch. 51 (the turnstile, the drain valve, the spinning cylinder) runs about 9% dialogue and ch. 59
(the Vecna vision and the ghoul pit) about 8% — both as low as anything in 78–83, both written by
you alone. Ch. 57, which is mostly the party talking to a water elemental and to Umberto, runs
about 22% in the same arc.

So a chapter that is one long corridor of rooms and fights will come in low, and that is fine. What
78–83 did was string **six** of them together with no talking chapter in between to reset. The fix
is not to force dialogue into a dungeon chapter — it's to make sure a dungeon run is broken up by a
Sarcelle, an Umberto, or a Tham.

## Yours vs. Claude's

Measured across the full 151,865-word pre-Claude corpus (chapters 1–77) against the drafted run.
Not everything in 78–83 is your voice; some of it is LLM house style that survived editing.

| Trait | Ch. 1–77 | Ch. 78–83 | Verdict |
|---|---|---|---|
| Spoken words as % of prose | 24.3% | 5.0% | **Regression — restore it** |
| `the [expression/posture/grip] of someone who…` | 0 uses in 151k words | 4.1 per 10k | Claude's tic, not yours |
| `the way a/one/you…` simile | 0.3 per 10k | 6.5 per 10k | Claude's, 20× amplified |
| Spaced em dash ` — ` | **0** in 151k words | 27.7 per 10k | Claude's — you type unspaced |
| Vague `something about/inside` | 0.3 per 10k | 7.3 per 10k | Claude's |
| `kind of` hedging | 0.3 per 10k | 4.9 per 10k | Claude's |
| `enough to/that` | 4.6 per 10k | 15.5 per 10k | Yours, over-amplified |
| `as though` | 3.4 per 10k | 4.1 per 10k | Genuinely yours |
| Mean sentence length | 16.3 words | 14.5 words | Improvement — keep |
| `-ly` adverbs per 1k | 18.0 | 13.9 | Improvement — keep |

**When drafting, actively suppress** the four "Claude's" rows and write dialogue near your
historical rate. **Keep** the tighter sentences and lower adverb count — those are real gains.

Em dashes are unspaced: `experience—and survival`. Your own reference note in the chapter files
gives the Mac shortcut (Option + Shift + Dash), so this is a deliberate habit, not an accident.

## Voice

**Third person, present tense, always.** "Mond hangs from a rung of the ladder." Past tense only
for things that already happened.

This holds across all 83 chapters — I checked, expecting the early ones to drift, and they don't.
Past-tense narration verbs sit near 7–11% of the total in every era of the campaign, including
chapters 1–13. The exceptions are exactly what the rule predicts: **a sustained history or
flashback passage goes fully past tense and then hands back.** Ch. 5's account of the Uprising and
the founding of the Hands of the Wand, and ch. 63's flashback, are the clearest cases — each about
half past tense, and each set off from the surrounding scene (ch. 5 puts it under its own italic
heading, `### _The Uprising..._`). That's the move: don't half-shift inside a paragraph, shift
wholesale for the whole passage and mark it.

**Short paragraphs, and single-sentence paragraphs as punctuation.** These do real work:

> Nothing happens.

> Then it stops.

> One remains.

> She sets the dead soldiers down gently.

**Dry understatement is the comic register.** The humor is never the narrator winking — it's a
flat, precise sentence about something absurd:

> It is a good hole. He's proud of it already.

> Bilwin raises his Mage Hand toward the blazebear with the optimism of someone who hasn't done
> the arithmetic on the weight involved.

> The stein misses, swinging through empty air with what can only be described as commitment.

> Mond fires at the last standing warforged and misses, his bolt going wide by enough that it's
> almost impressive.

**But dry understatement is the *late* register, not the only one.** The Elsemar chapters run on
puns and parody, and they are funny. Food Alley (ch. 19–21) is built entirely out of it: **Dolly's
Donuts**, **Eclairvoyant's Tea Shop**, **The Fizz Hutt**, and **Waffle Wizards** — a rundown
stone castle with an iconic yellow sign, whose manager dreams of being promoted to the Beyond the
Wall Grill or the Red Keep Bistro by the honchos at Game of Stones Restaurants. The jokes land on
the beat:

> "Do or donut, there is no try."

> "Now I'm glazed and confused."

> "Now, donut go causing too much a ruckus out there."

Ch. 19 is the whole mode in miniature — **242 words**, the shortest chapter in the campaign. The
party orders a dozen donuts, the donuts come alive and attack, Dolor eats the one that jumps into
his mouth because blueberry jelly is his favorite, and it ends on the pun. That's it. It works
because it doesn't overstay.

Helper NPCs get pun names too: the tabaxi guide **Rightside** ("Rightside will do ya right!") and
the tabaxi cartographer **Whichway** at a map shop called **The Four Corners**.

This register mostly disappears after Elsemar. It doesn't have to. A pun chapter is a legitimate
change of pace, and the campaign has gone a long time without one.

**Dialogue carries the story.** In chapters 56–77, spoken words are **24% of the prose**. The
characters talk — to each other, to NPCs, to corpses. Scenes advance through what people say.
See the "Yours vs. Claude's" section below: this is the single biggest thing to protect.

## Characters

Comedy and competence both come from character, never from the narrator:

- **Bilwin** — curiosity that outruns caution; walks into things first. Casts spells by accident
  and mostly gets away with it. Talks to the dead, badly. Never states a plan he hasn't already
  started executing.
- **Grindlefoot** — quiet competence, understated to the point of comedy. Digs a good hole. Reads
  terrain. Saunters toward combat "at a pace that suggests he is deeply unconcerned."
- **Gven** — direct, first through every door, and the narrative knows it costs her. She gets the
  interior monologue when one is warranted.
- **Dolor** — fastidious, analytical, keeps things to himself. Examines a dying warforged "the way
  he'd give a timepiece whose mechanism had gone still."
- **Mond** — showy, theatrical, a "predatory smirk." Occasionally says the tactless thing.

**The party in chapters 1–13 is not the party you know.** Bilwin and Mond do not exist yet. The
founding four are Dolor, Gven, Grindlefoot, and **Xantic, a gnome artificer** — plus McGillicutty,
the homunculus servant Xantic builds in ch. 7, who communicates only by pantomime and dances the
Carlton. Xantic is the engine of the early comedy: he stabs his own foot to test a healing potion,
blows up a child's doll with an eldritch cannon before anyone can stop him, cooks a "garbage
omelet," and knocks himself unconscious on a table before the Battle of Wayside so he misses the
whole thing.

**Bilwin and Mond enter in ch. 14**, walking the Ha-derech as strangers to each other and to
everyone else, arriving at Wayside just after the battle ends. In the same chapter Xantic leaves
for good, staying behind to protect the town. That is the roster changing over inside one chapter,
and it is handled entirely through scene — no announcement.

The group name also moves: **"the Mixed Nuts"** (Gven coins it under pressure in ch. 2) becomes
**"Chimera's Bane"** (Dolor renames them in ch. 7, waking from a dream). Grak still gets it wrong
in ch. 14: *"Well done, Mixed Nuts! Oops, I mean huzzah, Chimera's Bane!"*

When writing anything that reaches back before ch. 14, check who was actually there.

**Epithets are part of your voice, not a flaw to edit out.** "The dwarf," "the tiefling," "the
half-orc," "the sorcerer" appear **411 times across chapters 56–77** — 71 per 10,000 words. The
drafted chapters cut that to 24 per 10k, which is one reason they read as less like you.

Use them. The failure mode to avoid isn't using an epithet, it's stacking three different labels
for one character inside a single paragraph — Gven as "Gven," "the half-orc," and "the barbarian"
in four sentences. One alternate label per character per paragraph, then back to the name.

## Combat

Narrate outcomes, never numbers. Initiative rolls, per-round damage, and fight choreography live
in HTML comments; the prose says what happened in the world.

Compress. A round is not five paragraphs — it's the two or three actions that changed something.
Misses are worth a line only when the miss is characterful.

Failure gets specifics: "the first strike misses, the second lands clean and hard across the
warforged's midsection." Not "he attacks and hits."

Spells and rules terms are inline links to D&D Beyond, described in-world rather than named
mechanically where possible: "three crackling beams of energy," "a bolt of light," "his spiritual
beer stein."

A mid-combat interior beat is allowed and effective — Gven's paragraph in chapter 80 recalls the
chimera, the kraken, and the Hertilod before landing on "And this creature chose the wrong
barbarian," earning the kill that follows. One per fight is plenty.

## The round-robin — your signature structure

Outside combat, the move that recurs more than any other is **giving every companion an interior
beat in sequence**, one short section each:

- **Ch. 42** — each companion says why they're really on this journey, capped by Grindlefoot's
  "I'm looking for tasty nuts, really, that's about it"
- **Ch. 63** — four dreams after the first night in Lord Neverwinter's manor
- **Ch. 67** — five bath scenes, one per character, each surfacing a private preoccupation
- **Ch. 68** — four dream recollections, capped by Mond's joke that he slept fine
- **Ch. 76** — the warforged each answer "did you choose your name, or was it given?"

This is where the campaign's emotional continuity lives: Bilwin's lost dwarven company, Gven's
brother, Mond's freedom to use magic openly, Grindlefoot's spider-self, Dolor's parents' workshop.
Combat advances plot; the round-robin advances character.

Use it at every rest, arrival, or downtime beat. Vary the frame — dreams, baths, a shared question,
a quiet evening around Dolor's glory hole. Chapters 78–83 contain **none** of these, which is a
bigger loss than the dialogue drop.

## Non-combat chapters are a mode, not a gap

Chapters 63, 74, and 75 have essentially no fighting and are among the strongest in the run: the
two months settling into Neverwinter and the arrival of Eva Brightbroom; Tasha turning Gven into a
goldfish and letting her suffocate to teach her manners; Grindlefoot scrying his garden through a
potato; Bilwin's three yes-or-no questions to a drunk Hanseath.

Don't treat a session light on combat as a thin chapter. It's an opportunity.

## NPC voice is the craft

Every named NPC gets a distinct verbal signature, and they're the most memorable thing in the
campaign. This is the hardest thing to imitate and the most important to get right:

| NPC | Register |
|---|---|
| Gertrude (cyclops) | Three-to-five-word sentences. "I'll smash for you!" "Mine." "Go find friend. After smash." |
| Redbud (treant) | `...One ...word ...at ...a ...time`, literally typed that way |
| Ikasa (blink dog) | Excited fragments, dog logic. "You smell like fire. I like it." |
| 404 (warforged) | Error messages. "Name not found!" "Purpose found!" |
| Captain Inda | Heavy phonetic pirate. "Aye, so might a skulking bilge-rat…" |
| Tasha | Arch and camp. "Speak for yourself, darling. Some of us are _always_ fabulous." |
| Eva Brightbroom | Mary Poppins, never once acknowledged. "I never explain anything." |
| Hanseath | Drunk god who breaks the fourth wall on game rules |
| Maltok | Flat, literal telepathy. "Feels sturdy. It would work in battle. And kill fish." |
| Gustaf Mondalbrot | Verbose archaeologist; digresses, name-drops his own adventures, undercuts himself |
| Nyx (tabaxi) | Laconic, dry. "I got hungry." Feline tells slipped in — a purr, a lope |
| The sphinx | Bored and deadpan; answers only what it was built to answer |
| Dave Chevits | Fences with knitting needles; opens by disambiguating themself from David Shevitz |
| Tham (Thamnoki Grumblebuster) | Heavy phonetic Scots, every line. "Ach, aye. This is whit I wis lookin' for! Cannae leave wi'oot some scran, noo can I." |
| Cap'n Don Karnahge | Phonetic Scots plus delight in his own machinery. "It wirks! It really wirks!" Two rules on his ship, and rule one is "dinnae faw aff" |
| Cindel | Self-mythologizing. "Huzzah!", a billowing cape, and a shaft of sunlight that finds her *and only her* on an overcast day |
| Xantic | Gnome artificer, ch. 1–14. Curiosity with no brakes and no sense of consequence |
| Rightside (tabaxi) | Helpful, eager, and derails mid-sentence whenever light catches something shiny — held consistently across ch. 16, 24, 26 |
| Grak (goblin) | Takes offense at everything, wears no pants, and is deadly serious about both. "It's time for my pants." |
| Hanseath, in person (ch. 32) | Spills half of every drink into his beard. "Dig deep enough, and the mountain's always there." Then: "Now, what the fuck are you doing?" |
| Fred (half-orc pastry chef) | Slow, dry, delivers puns without acknowledging them |
| Whelm (warhammer) | Telepathic, olde dwarven, single-minded about giants. "Aye, lad! Where them giants be hidin'?" |
| Umberto Noblin | Gnome historian; answers a question by first listing his own book titles |
| The water elemental (ch. 57) | Telegraphic pidgin, arriving through Dolor's translation. "No mood for fighting today. Friend offer escape, but tiny. No fit." |

Give every new NPC one rule like this and hold it for every line they speak.

**Phonetic Scots is your most-reused dialect, and it is getting crowded.** The tortle at the Hall
of Records (ch. 16), Cap'n Don Karnahge (ch. 22–34), and Tham (ch. 52) are all written the same
way, and Captain Inda's pirate is adjacent. Two of them carry working notes in the file — ch. 16
links a Scots translator, ch. 34 keeps a plain-English version of Don's speech in a comment — so
this is a deliberate tool, not an accident. It is effective and it is a lot of work to read. Before
reaching for it a fifth time, give the new NPC a different axis: a rhythm (Gertrude's three-word
sentences), a formatting tic (Redbud's `...one ...word ...at ...a ...time`), or a category error
(404's error messages). Those distinguish an NPC without taxing the reader.

Two of these are worth noting as a pattern in their own right: **magic items talk.** Whelm nags
Bilwin through three straight chapters (50, 51, 52), always about giants, always at the wrong
moment. Wave introduces itself to Dolor with four words and nothing else: *"I am Wave."* A sentient
item gets the same treatment as an NPC — one rule, held.

Bilwin's running gags recur across chapters and should be reached for rather than reinvented.
Ch. 56 has him spelling out "sar-kay-oh-ef-uh-guy" so the wights won't know what the party is
after, and the joke gets picked up twice more in the same chapter, including as its closing line.

## Puzzle and set-piece chapters

A whole mode the Mournland arc has little of. Chapters 41–52 are built around them, and they're
some of the most inventive writing in the run:

- The seasons door in ch. 41, solved as an exclusive-binary operation
- Offerings placed in a god's four open hands, ch. 42
- The sphinx's riddle at the three-way junction, ch. 45 — and its deadpan follow-up after the party
  walks into a pit: *"There's a pit down that passage."*
- Golems numbered 5, 7, 9, 11, 13 — pick the one that doesn't belong, ch. 48
- Nine orbs, one real key, ch. 49
- Timing two geysers on a 5-minute and 3-minute cycle to cross hanging discs, ch. 49
- A one-way turnstile with no reverse, ch. 51
- A ten-foot pool with a valve wheel at the bottom that drains the level, ch. 51
- A thirty-foot spinning cylinder painted like a barber's pole, greased, with a fire trap that
  triggers on contact, ch. 51
- A translucent bubble holding back a cavern of boiling water, with a giant crab guarding the
  trident Wave in the sand at its center, ch. 52

**Two solution modes, and the second is at least as common as the first.**

*Solved.* A character reasons it out aloud, and the reasoning is the scene — not narration
explaining it afterward. Dolor gets "I think it's more complex, most likely an exclusive binary
operation"; Mond asks for ten minutes and comes back with "the geyser closest to us erupts every
5 minutes… and the geyser on the far side, every 3."

*Bypassed.* Just as often the party refuses the puzzle on its own terms and goes around it with an
ability or with muscle — and the writing gets its comedy from **what the bypass costs**:

- Ch. 50 abandons the geyser timing entirely once the rope is destroyed. Grindlefoot wild-shapes
  into a giant spider and ferries everyone across the ceiling in butt-yarn. It works — except
  Golem Number 9 is too heavy, the webbing snaps, and the golem sinks into the boiling mud, calm
  the whole way down, waving at Gustaf before it goes under.
- Ch. 51 answers the turnstile with Mond freezing it brittle and Gven and Dolor snapping it, which
  leaves her slumped on the floor in exhaustion.
- Ch. 51 answers the spinning cylinder with Dolor simply going in — he slips, ends up prone, the
  floor bursts into flame under him, and he rolls out the far end. "If it's not a rope it's
  something else."

Neither mode is the correct one. The bypass is not a failure state to write around: it produces
Grindlefoot's spider ferry and Dolor's second bad experience with being tied to things, and those
are better scenes than a clean solve would have been. Write whichever one the table actually did,
and make the cost visible.

## Verse

Prophecies and riddles are set as markdown blockquotes with `<br>` line breaks (ch. 45, 47, 48,
50). The White Plume prophecy runs five stanzas. Gustaf's reaction is the model for how to undercut
your own verse: *"the author could have used an editor. Evocative imagery and clear structure, but
the cadence is uneven and phrasing repetitive."*

The blockquote is not only for verse. Ch. 20 gives four full paragraphs of blockquote — no `<br>`,
no line breaks — to Thistlewick Brandlestrum climbing onto a stool to deliver an unhinged oration
about **kombucha**: "the elixir of the enlightened, the nectar of the ancients… a celestial tango
of opposites that finds unity in your mouth." Nothing plot-relevant happens in it. It is a comic
aria, and the blockquote is what marks it as a performance rather than dialogue. Use the form when
a character delivers a set piece, not just when something rhymes.

## Banter inside combat

Fights are not tonally sealed off. In ch. 47 a black knight and Gven trade skincare advice
mid-melee — *"You really need a better skin care routine"* … *"It's a special compound of
all-natural, organic ingredients that I apply twice a day."* Combat is where character comedy
happens, not a break from it.

## Markers and devices

- `_The group has learned the secret of X, …_` — italic, closes a secret-learned beat. First used in
  ch. 56, then 57, 65, 70, 71, 76. The `secret-learned` tag is on one more chapter than the marker
  is (ch. 59, where the party receives Vecna's gift but no italic line closes it)
- `_The adventurers advance to level N._` — italic, ends the chapter
- `Long rest....` / `Short rest....` — four dots, on its own line
- `_Guest player: Name as Character_` — italic credit at the end
- Player-drawn maps embedded as images, credited to Mond or Gustaf

## Profanity

Used sparingly and always as a punchline or a pressure release, never as texture. "Well, fuck."
ends chapter 63. Elden shrugs "Fuck you all" and jumps into a portal. Kycera's "Get that fucker!"
launches a fight. Grindlefoot's "Do you want to fuck yarn or do you want this?" is the biggest
laugh in the run. Keep it rare enough that it lands.

## Emotional scenes

Slow down and cut the sentences shorter. The Mercy/Filch reunion in chapter 78 is the high-water
mark: "No one speaks." / "Mercy stays there for a long time." / "The companions wait without
fidgeting, without filling the silence."

Let silence be described rather than filled. Then undercut it — that scene ends on "Mercy. Where
the hell have you been?"

## Chapter shape

**Open mid-motion**, continuing directly from the previous chapter's final beat. 79 opens in the
quiet after Filch's revival; 81 opens with Dolor still pinned under the blazebear.

**Close on a button** — a joke, a reveal, or an image that hangs:

> It lands directly on Dolor.

> "Mercy. Where the hell have you been?"

> The woman on the bunk doesn't move.

Scene breaks are `---` on its own line, used freely — chapters 78–83 average five or six.

Housekeeping stays terse: `Long rest….`

Guest players get a trailing italic credit: `_Guest player: Kimber Hilton as Mercy, the warforged_`

The device starts at ch. 39 and has been used five times: ch. 39 and 42 (Nyx Whiskerfang, played by
two *different* guest players — Chris Sells, then Kimber Hilton), ch. 47 (Dave Chevits), and ch. 77
and 78 (Mercy). A recurring guest character surviving a change of player is worth remembering: the
character belongs to the campaign, not to the guest.

## Continuity

Reach back. Chapter 80 calls on the chimera, the kraken, and the Hertilod from the god's heart.
Chapters 81–82 build Dolor's parents-built-this-colossus thread across two sessions. NPCs are
remembered by name and their earlier behavior. Check the appendix
(`_posts/2023-01-23-appendix.md`) for people, places, and history before inventing a detail.

**Origins worth knowing, since the signature items all come from chapters 1–39:**

- **Gleaming Blade** is looted off a goblin corpse in ch. 7 and mistaken for a rusty old sword;
  Dolor attunes to it in ch. 9 and learns it belonged to a paladin.
- **Tempest Edge** is a *gift* from **Veylara**, a storm giant, in ch. 32 — it is her boot dagger,
  sister-forged to her own greatsword, and it is longer than Gven is tall. **This debt is still
  open.** Gven promised to return the blade one day, and Veylara holds her family's Gruumsh
  medallion — carved by Gven's father — as the counter-gift, worn as an earring. Any scene that
  wants to land on Gven should know this exists.
- **Bilwin's hurdy-gurdy** spends thirty chapters as a joke — he plays it terribly and mostly uses
  the case as a club — until ch. 34 and 37, where he plays beautifully in Dwarven and only Gven
  can understand the words. The instrument being genuinely good when it matters is a setup that
  took a very long time to pay off.
- **Torp is Davanor** (ch. 28), Gven's brother turned zealot, planning the genocide of every magic
  user in Eritz. Gven's whole reason for being on the road in ch. 1 is looking for him.

## Chapter openings

**28% of chapters (22 of 80) open with a participial recap phrase** — "Having defeated the animated
pastries…", "After vanquishing the gnolls…", "Standing in front of the entrance…", "Looking for any
signs of weakness…". It's an effective "previously on" device and unmistakably yours, but at better
than one chapter in four it has become predictable.

Vary it. Chapters that open cold on an image or a line of dialogue are among the strongest in the
run — ch. 31 opens on `"You're an interesting sight."`, ch. 63 on `"Pardon me, your brother?"`.

## Endings

**34% of chapters end on a line of dialogue.** That's your most consistent structural signature
across all 80 chapters, and it's usually a joke or a character beat: "Where the fuck have you been,
Torp?" / "Now I'm glazed and confused." / "Smells like barbeque." / "that wasn't optimal."

Other endings in use: `_The adventurers advance to level N._` (10 chapters), `Long rest….`, and
occasionally a closing image.

Watch for repetition. **Chapters 45, 46, 48, 49, 50, 51, and 52 all end with the same map image and
the identical caption** — seven of the eight chapters in that span. (Ch. 47 carries the map too but
ends on a guest-player credit instead, and ch. 43 and 44 break the run before it starts.) Whatever
else varies, vary the last beat.

The framing device around those maps does vary, and that's what saves them: Gustaf sits down to
update the map while the others rest (ch. 50), narrates his own enthusiasm (ch. 51), or hides in the
entry passage insisting the party surely has the giant crab under control (ch. 52). In ch. 50 the
map beat carries real weight — Gustaf is quietly mourning Golem Number 9, the "kindred cartography
spirit" who drowned in the mud an hour earlier.

## Crutches worth watching

Measured across chapters 56–77. None of these are wrong; all are load-bearing enough to notice.

| Crutch | Rate | Note |
|---|---|---|
| `suddenly` | 6.7 per 10k | Usually deletable — the event is already sudden |
| `slowly` | 6.5 per 10k | |
| `quickly` | 6.0 per 10k | |
| `slightly` | 5.7 per 10k | Hedges the image it modifies |
| `immediately` | 5.3 per 10k | |
| `begins to` + verb | 7.3 per 10k | "begins to walk" → "walks" |
| `seems to` | 5.4 per 10k | Hedge |
| `appears to be` | 4.2 per 10k | Hedge |
| `the group/party/companions decides` | 25 uses, 24 chapters | See below |

**Correction to an earlier draft of this file:** "the party decides to…" was listed as a *don't*,
on the reasoning that characters act and groups don't deliberate on the page. That is not supported
by the corpus. The construction appears about 25 times across 24 chapters, spread evenly from ch. 3
to ch. 80 — including in the drafted run. It is a genuine, low-frequency habit, roughly one use
every three chapters, not a foreign tic.

It is still worth watching, because it does flatten a beat when the alternative was available. Ch.
51's "The rest of the party decides to remain on the original side" is the weak form. Ch. 58's
answer to the same problem is the strong one: "Gven votes with her feet, opening the previously
hidden door in the south wall" — a character settles the group's decision by acting, and the
sentence is funnier for it. Prefer that when it's within reach. Don't hunt down every instance.

Those five adverbs total roughly **30 per 10,000 words** — about one every twelve sentences. The
drafted chapters cut the hedging verbs to near zero, which is a genuine improvement worth keeping.

## Abandoned experiments — don't revive

- **List-form combat.** This was a much bigger and later thing than an earlier draft of this file
  recorded, and the sequence ran the other way. The real history:

  | Chapters | Combat form |
  |---|---|
  | 1–4 | Prose. Ch. 1 puts it under a rendered `## Fight choreography` heading; ch. 2–4 keep the mechanical list in `<!-- Step-by-step -->` comments and write prose from it |
  | 6–36 | **Rendered bulleted lists were the published combat text** — one bullet per turn, damage numbers on the page, under a visible `## Fight choreography` H2 |
  | 38, 39, 43 | Prose again, list demoted back into `<!-- Step-by-step -->` comments |
  | 44–83 | Prose only, mechanics entirely in comments |

  Twenty chapters carry the rendered heading: 1, 6, 7, 8, 9, 10, 12, 13, 14, 17, 21, 25, 27, 29,
  30, 31, 33, 35, 36, 38. Ch. 13's Battle of Wayside runs twelve numbered rounds as a pure list.
  So the `<!-- Step-by-step -->` blocks at 38/39/43 are not residue of an abandoned start — they
  are the **transition back out** of a thirty-chapter published-list era, the last stage before
  the mechanics disappeared into comments for good.

  The conclusion is unchanged and now better supported: **prose won, and it is not close.** Ch. 13
  as a list is unreadable next to ch. 35's jungle or ch. 38's grung fight. **Do not create
  `<!-- Step-by-step -->` sections and never render mechanics on the page.** But know that the
  early chapters look the way they do because that *was* the format, not because they were
  drafts.

  Two heading variants show the form was used for more than fights: `## Encounter choreography`
  (ch. 10, the stealth rescue of Vera from the hill giant) and `## Storm choreography` (ch. 30,
  eight rounds of the crew climbing masts in a gale). The storm one is genuinely effective as a
  structure — a non-combat set piece with initiative and rounds — and is worth remembering as a
  way to stage a group physical crisis, even though it should be written as prose now.

- **Bulleted lists** appear in 18 chapters, all at ch. 36 or earlier (loot tallies, mostly). You
  stopped, and the prose is better for it — with **one deliberate exception**: ch. 58 sets out what
  Dolor finds in the necromancer's marginalia as a four-item list (the tangible quality of secrets,
  the siphoning ritual, the first test subject, the Crevices of Dusk). That one earns it. A list of
  *discovered documents* reads as the party's findings rather than as a session log, and it hands
  the reader four plot facts they'll need later without a paragraph of throat-clearing. Reserve the
  form for that: notes, ledgers, and research the characters are reading — never for what the party
  did or what it looted.
- **`<details>` collapsible blocks** appear only in chapters 25 and 28 — and they are not a prose
  device at all. They hold an author-facing *synopsis* of the chapter, bulleted, written when the
  prose wasn't finished in time. Ch. 28 says so in a comment: "The following summary was
  temporarily written up, giving me time to fully vet the conversation between Gven and Torp."
  Useful to know as a stopgap; the two that shipped were never replaced with prose.

- **The narrator addressing the reader** was recorded here as happening exactly once, in ch. 16
  ("_For brevity's sake, the narrator has left out much of the dialog…_"). **That is wrong.** Ch.
  16 is the most explicit instance, not the only one. Direct second person to the reader shows up
  in narration at least four more times, all early:

  > You note that the patrons treat the younger woman with respect, not the typical bawdiness you
  > might encounter in such a crowd. *(ch. 2)*

  > You don't mess with the Pride and Comfort without experiencing the consequences. *(ch. 5)*

  > There are still plenty of ways to spend your hard-earned coin… *(ch. 22)*

  > Rightside looks as you'd expect a wet cat to look. *(ch. 26)*

  There is also a narrator's conspiratorial "…, mind you" in ch. 20, 24, 34, and once as late as
  ch. 74. The habit fades after the Elsemar arc rather than stopping dead. **Still don't do it** —
  the guidance was right even though the history wasn't — but don't be surprised to find it, and
  don't "fix" it in an old chapter.

## Proofreading

Chapters 60–77 carry roughly 48 recurring misspellings. `halfing` for `halfling` alone appears 11
times. Others that recur: `concious`, `acquiesence`, `irridescent`, `death throws` (for "throes"),
`occured`, `catastrophy`, `posessions`, `accomodations`, `demeaner`, `respit`.

None of it hurts the storytelling, and the voice is strong enough to carry them — but a spellcheck
pass before publishing is the single cheapest improvement available. Watch `halfing` especially;
spellcheck may not flag it.

One a spellcheck will never catch: **Nyx's surname is spelled two ways.** Ch. 39's prose calls him
"Nyx Whisperfang" four times, while its own guest-player credit — and ch. 41 and 42 — say
"Whiskerfang." Whiskerfang is the one that stuck. Same class of error to watch for with any name
introduced mid-fight.

## Don't

- Bulleted or summarized session recaps
- Dice numbers, hit points, or rules math in the prose
- Second person, or any authorial aside to the reader
- Narrating every single attack (that's the pre-78 mode)
- Three different labels for the same character inside one paragraph
