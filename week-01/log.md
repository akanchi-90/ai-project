# Week 1 log

## Day 1 - 2026-11-17
- Topic: setup and baseline
- Installed uv 0.13.9 and Python 3.12.16 (via `uv python install 3.12`)
- Q: Why "uv: command not found" after installing? → the terminal was opened before
  ~/.zshrc was updated; open a new terminal or `source ~/.zshrc`
- Rated 15 skills in baseline.md (Python 0, maths 4, system design 3, …)
- Committed: baseline.md ("baseline Updates")

## Day 2 - 2026-11-18
- Topic: Python environment and first code
- Created .venv with `uv venv --python 3.12`; added .gitignore (`.venv/`); pinned 3.12
- Q: What does uv do? → manages Python versions, virtual envs and packages in one tool
- Q: Can I default to 3.12? → pin per project (`uv python pin 3.12`) rather than globally
- Q: Why doesn't `code day.py` work? → `code` wasn't on PATH; added VS Code's bin folder to ~/.zshrc
- Q: What is a CLI? → a program driven by typed commands: program + subcommand + options
- Q: Arguments vs variables? → variable = named value; parameter = variable in a def;
  argument = the value passed in a call
- Committed: week-01/day1.py ("first hello world code")

## 2026-11-21 - tooling
- Connected GitHub to Claude; set up a daily 7:30 AM ET recap email (cloud routine + Gmail)
- Learned: a terminal reads its startup files only when it opens; PATH is the list of folders searched for commands
- Next: CS50P lectures 0–1 and problem sets 0–1 (plan Day 2)
