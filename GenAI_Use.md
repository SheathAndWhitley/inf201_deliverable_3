# Use of Generative AI – Deliverable 3

## Tools used

| Tool                            | Model           | Used for                                                               |
| ------------------------------- | --------------- | ---------------------------------------------------------------------- |
| Claude Code (VS Code extension) | Claude Opus 5.5 | Reviewing the finished code against the assignment, drafting this file |

## Summary of use

### 1. Writing the code (Tasks 1–5)

- Claude was used to review my code after writing each task, it was never used to directly write or edit a file only give feedback

### 2. Final review before hand-in (Claude Code, 9 Nov 2026)

When the code was finished, we asked Claude Code to read the assignment again (`deliverable_03-1.pdf`)
and check whether our scripts met all requirements. The assistant:

- Read all modules and the notebook, and compared them with each task in the assignment.
- Ran some edge cases against our classes. It found that `heal()` with a negative amount and
  `take_damage()` with a negative amount can push HP outside the range `0 … hp_max`, which breaks the
  game rule that HP must always be between 0 and the character's max.
- Pointed out missing hand-in items: `requirements.txt`, `git_log.txt`, a PDF of the notebook, the GitHub
  link and the video.
- Noted that the assignment names the module `items.py`, while ours is called `rpg_items.py`.
  - Was renamed to make the repo tidier having all class scripts grouped together
- Drafted this `GenAI_Use.md` file. The parts about our own earlier work are left for us to fill in,
  since the assistant had no record of them.
