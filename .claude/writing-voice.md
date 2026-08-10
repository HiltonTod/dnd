# Writing voice

Derived by reading chapters 78–83 (the Claude-drafted, hand-edited run) against chapter 77 (the
last fully hand-written one). Quotes below are verbatim from the repo. This file exists so the
voice lives in the repo rather than in any one tool's memory.

## The workflow that produced these

From your own note in `2026-05-04-chapter-78.md`:

> This chapter was drafted by Claude. I had Claude review the 77 chapters I had written to
> understand the storylines, characters, and my writing style. I dictated my notes into a Google
> Doc, pasted that into Claude, and had it write a first draft, then a second. I manually edited
> the final draft, putting my own touches and style on it.

Two drafts, then your edit. The second draft matters — the first one gets the events down, the
second one finds the beats. Don't hand over a first draft as though it's finished.

## What changed at chapter 78

The break between 77 and 78 is sharp, and everything after 78 keeps the new shape:

| | Ch. 77 and earlier | Ch. 78 onward |
|---|---|---|
| Combat | Every attack narrated, round by round | Compressed; only what turns the scene |
| Paragraphs | Dense, 5–8 lines | Short, often 1–3 sentences |
| Line endings | Hard-wrapped at ~120 chars | No hard wrapping, one line per paragraph |
| Em dash | Unspaced — `experience—and survival` | Spaced — `already made — it shows in their bearing` |
| Emotional beats | Summarized | Given room, sometimes a full scene |
| **Dialogue** | **24% of prose is spoken words** | **5%** |

Match the newer column on compression and paragraphing. **Do not match it on dialogue** — see below.

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

Give every new NPC one rule like this and hold it for every line they speak.

## Markers and devices

- `_The group has learned the secret of X, …_` — italic, closes a secret-learned beat (ch. 65, 70, 71, 76)
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

## Continuity

Reach back. Chapter 80 calls on the chimera, the kraken, and the Hertilod from the god's heart.
Chapters 81–82 build Dolor's parents-built-this-colossus thread across two sessions. NPCs are
remembered by name and their earlier behavior. Check the appendix
(`_posts/2023-01-23-appendix.md`) for people, places, and history before inventing a detail.

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

Watch for repetition. **Chapters 45, 46, 48, 49, 50, 51, and 52 all end with the identical map
image** — seven chapters in a row closing on the same caption. Whatever else varies, vary the last
beat.

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

Those five adverbs total roughly **30 per 10,000 words** — about one every twelve sentences. The
drafted chapters cut the hedging verbs to near zero, which is a genuine improvement worth keeping.

## Abandoned experiments — don't revive

- **Bulleted lists** appear in 20 chapters, nearly all before ch. 36 (loot tallies, mostly). You
  stopped, and the prose is better for it.
- **`<details>` collapsible blocks** appear only in chapters 25 and 28.
- **The narrator addressing the reader** happens exactly once, in ch. 16: "_For brevity's sake, the
  narrator has left out much of the dialog…_" Never repeated.

## Proofreading

Chapters 60–77 carry roughly 48 recurring misspellings. `halfing` for `halfling` alone appears 11
times. Others that recur: `concious`, `acquiesence`, `irridescent`, `death throws` (for "throes"),
`occured`, `catastrophy`, `posessions`, `accomodations`, `demeaner`, `respit`.

None of it hurts the storytelling, and the voice is strong enough to carry them — but a spellcheck
pass before publishing is the single cheapest improvement available. Watch `halfing` especially;
spellcheck may not flag it.

## Don't

- Bulleted or summarized session recaps
- "The party decides to…" — characters act, groups don't deliberate on the page
- Dice numbers, hit points, or rules math in the prose
- Second person, or any authorial aside to the reader
- Narrating every single attack (that's the pre-78 mode)
- Three different labels for the same character inside one paragraph
