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

First names only. No epithet-juggling — "the dwarf" and "the tiefling" appear, but sparingly, and
never three different labels for one character in a paragraph.

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

**One interior beat per chapter, at most.** The model is Gven's paragraph in chapter 80 — a
mid-combat recollection of the chimera, the kraken, the Hertilod, landing on "And this creature
chose the wrong barbarian." It earns the kill that follows. Overusing this would wreck it.

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

## Don't

- Bulleted or summarized session recaps
- "The party decides to…" — characters act, groups don't deliberate on the page
- Dice numbers, hit points, or rules math in the prose
- Second person, or any authorial aside to the reader
- Narrating every single attack (that's the pre-78 mode)
- Three synonyms for the same character in one paragraph
