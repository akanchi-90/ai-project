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

## Day 2 (cont.) - 2026-11-23
- Topic: CS50P lectures 0–1 (functions, variables, types, conditionals, exceptions)
- Wrote day2.py (input + int), day2problems.py (20-question quiz), day2compare.py
- Q: Why "can't open file week01/day2.py"? → I was already inside week-01, there was a typo (week01), and the file wasn't created yet; check with pwd / ls
- Q: int vs float vs round? → int() chops the decimal, float keeps it, round() rounds; exact .5 rounds to the even number (round(2.5)=2, round(1.5)=2)
- Q: What are f"{x:.2f}" and f"{x:,}"? → format codes: 2 decimals / thousands commas; round() gives a number, f-string gives text for display
- Q: Function vs class vs method? → function: name(); class: blueprint/type (int, str); method: function on an object, obj.name()
- Q: What is scope? → assigning inside a function makes a local variable; the global is untouched (UnboundLocalError trap); pass in + return out instead of `global`
- Q: What does return do? → hands a value back and exits; no return gives None; the value is lost unless saved (count = bump(count))
- Q: What is `**`? → power, groups right to left: 2 ** 3 ** 2 = 512; -2 ** 2 = -4
- Q: What is `//`? → floor division, rounds down: 7 // 2 = 3, -7 // 2 = -4
- Q: Is the `.` operator only for strings? → no, every type has methods ((2.5).is_integer(), dir(int))
- Q: if/elif/else, and/or, match? → first True branch wins; and/or are lowercase; match/case with | and _ for exact values
- Q: Why did print(input(int("Age: ")) + 25) fail? → calls run inside-out; it should be int(input(...))
- Covered lecture notes: exceptions (try/except/else/pass, get_int loop), main() pattern, default params, Pythonic `return n % 2 == 0`
- Quiz misses to review: T1/T10 round-half-even, T2 `**` order, T4 "5"*3, T6 unsaved return, T9 0.1+0.2 != 0.3
- Committed: day1.py, day2.py, day2problems.py, day2compare.py ("Day 2", "Day 1")
- Next (Day 3): finish quiz T3/T5/T7/T8 + E3 fixes; exercises C1–C4, X1–X3, day2final.py; CS50P problem sets 0–1
