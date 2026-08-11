# Dungeons & Flagons

Session notes for an ongoing D&D campaign, published as a Jekyll site at
<https://todhilton.com/dnd/>. Sessions run roughly every two weeks; each one becomes a chapter.

The party: Bilwin (dwarf cleric/bard), Dolor Vagarpie (tiefling rogue), Grindlefoot (halfling
druid), Gven Vetkam (half-orc barbarian), Mond Blue (half-elf sorcerer). World is Olam;
the continent is Eritz.

## Layout

| Path | Contents |
|---|---|
| `_posts/` | Everything. 88 files: 81 chapters, 6 character posts, 1 appendix |
| `_pages/` | `about.md` plus the archive pages (category/tag/year) and 404 |
| `_data/navigation.yml` | Top nav |
| `assets/images/` | Maps, handouts, screenshots |
| `_config.yml` | Site config; theme is `mmistakes/minimal-mistakes` via `remote_theme` |

There are no `_layouts` or `_includes` — everything comes from the remote theme.

## Posts

Filename is `YYYY-MM-DD-chapter-N.md`, where the date is the **session date**, not the writing
date. Chapters are numbered sequentially and never renumbered.

Three categories, and a post has exactly one:

- `campaign` — chapters (81)
- `adventurers` — one post per player character (6)
- `notes` — the appendix (1)

Front matter for a chapter:

```yaml
---
title: "Chapter 83"
show_date: true
date: 2026-07-20T17:00:00-00:00
sessiondate: "July 20, 2026"
modified: 2026-07-20
categories:
  - campaign
tags:
  - eve-of-ruin
  - fight
  - mournland
---
```

`title`, `show_date`, `date`, `categories`, and `tags` appear on all 88 posts. `sessiondate` is
on the 82 session-derived ones. `modified` is set when a post is revised after publishing.

Tags are lowercase-hyphenated and do real navigational work — the tag archive is a main nav item.
They mix arc names (`eve-of-ruin`, `rod-of-seven-parts`), locations (`mournland`, `elsemar`,
`wayside`), NPCs (`landro`), and event types (`fight`, `levelup`, `secret-learned`,
`guest-player`). Reuse an existing tag rather than coining a near-duplicate; check
`grep -h -A20 '^tags:' _posts/*.md | grep '^\s*-' | sort | uniq -c | sort -rn` first.

## Writing chapters

**Read `.claude/writing-voice.md` before drafting or editing any chapter prose.** It documents the
voice in detail, derived from a full read of all 83 chapters, with examples. Alongside it:
`.claude/characters.md` (what the party look like and how they carry themselves),
`.claude/story-so-far.md` (arcs, character threads, what's still unresolved), and
`.claude/to-do-list.md` (tracked fixes).

The short version: narrative prose, third person, **present tense** ("Mond hangs from a rung of the
ladder…"), past tense only for things that already happened. Recent chapters run 2,000–4,600 words.
Characters go by first name. It reads as a story, not a bulleted session log — no "the party then
decided to." Dice outcomes are narrated as events, never as numbers in the prose.

`---` on its own line marks a scene break (used in about half the chapters — where the session had
distinct scenes).

Links to D&D Beyond for monsters, spells, and rules are common and welcome.

### Session notes live in HTML comments

83 of 88 posts carry `<!-- ... -->` blocks that don't render: initiative rolls, round-by-round
fight choreography, `<!-- NOTES -->` scratch, and reference cheat-sheets the author keeps handy
(em dash character, frequently-used links, ship direction glossary). **Preserve these when
editing.** They're the raw material behind the prose — treat them as the author's working notes,
not as cruft to clean up.

### The Claude tag

Chapters 78–83 carry the tag `co-written-with-claude`. **If you help write or substantially revise
a chapter, add that tag.** It's how the author tracks provenance. (Distinct from `ai-generated` on
`2025-09-01-chapter-62-ai.md`, a one-off fully-AI alternate version of chapter 62 published
alongside the human-written one.)

Chapter 78 was the first Claude-drafted chapter — its trailing comment says so — and went untagged
for a while; it was tagged retroactively, so the drafted run 78–83 is now consistent.

## Internal links — read this before writing any

The site is served from a subpath, but `_config.yml` sets **no `baseurl`**. Every internal link is
therefore written with a hardcoded `/dnd` prefix:

```markdown
[ch. 14](/dnd/campaign/chapter-14/)
![Wayside's layout](/dnd/assets/images/town-wayside-layout.png)
```

Permalinks resolve as `/:categories/:title/`, so chapter 83 lives at `/dnd/campaign/chapter-83/`
and a character at `/dnd/adventurers/bilwin/`.

Some older links use the absolute form `https://todhilton.com/dnd/...` instead. Both work. Match
the surrounding file; prefer the root-relative `/dnd/...` form in new writing.

## Build and deploy

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/dnd/
```

Deploy is a push to `main` — GitHub Pages builds it. There is no CI and no build step to run
before committing. Because the `github-pages` gem pins versions, a plugin that works locally may
still be unavailable on Pages; stick to the plugins already listed in `_config.yml`.

Note `jekyll-algolia` is in the `Gemfile` but not in `_config.yml`'s plugin list — search comes
from the theme's built-in Lunr, not Algolia.
