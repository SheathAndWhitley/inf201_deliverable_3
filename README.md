# INF201 – Deliverable 3: RPG Battle Simulator

A small turn-based battle simulator built with object-oriented Python
(encapsulation, composition, inheritance).

Repository: <https://github.com/SheathAndWhitley/inf201_deliverable_3>

## Contents

| File | Description |
|---|---|
| `rpg_dice.py` | `Dice` – n-sided die (n ≥ 2), `roll()`, `__call__`, `__repr__` |
| `rpg_items.py` | `Weapon` – name + damage `Dice`, `roll_damage()` (the assignment's `items.py`) |
| `rpg_character.py` | `Character`, `Warrior`, `Mage` |
| `rpg_battle.py` | `Battle` – `play_round()`, `simulate_battle()` |
| `rpg_simulator.ipynb` / `.pdf` | Presentation of each class and simulated battles |
| `GenAI_Use.md` | Discussion of generative AI use |
| `git_log.txt` | Commit log |
| `game_simulator_v1.py`, `game_rules.txt`, `deliverable_03-1.*` | Starting code and assignment text |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then open `rpg_simulator.ipynb` and select the `.venv` kernel. The modules use only the
standard library; `requirements.txt` lists the Jupyter kernel packages.
