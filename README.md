# operant-league

A fast-and-dirty command-line tool for operant-conditioning yourself: gate your League of Legends matches (or any reward) behind a random, variable-ratio number of completed real-life tasks.

## What it does

Behavioral psychology says a **variable-ratio reinforcement schedule** — a reward delivered after an unpredictable number of actions — is one of the most powerful ways to reinforce a behavior (it's the same mechanism slot machines use). This tool applies that to productivity.

When you start it, the program picks a secret random target between `MIN_TASKS` and `MAX_TASKS`. You mark real-life tasks as "done" one at a time; once you hit the hidden target, you've "earned" a League of Legends match. It then rolls a new random target and the cycle repeats. Every action is timestamped to `task_log.txt`.

The script does **not** launch League for you — it's an honor-system tracker. When you earn a match it just tells you to go play.

It's an interactive menu:

1. Mark a task as completed
2. Check current status (only works if `--show-status` is enabled; otherwise it prints a notice that status display is disabled)
3. Reset the target manually (only allowed if `--target-changeable` is enabled)
4. Exit

## Requirements

- **Python 3** (tested with 3.12; anything 3.6+ should work).
- No third-party packages — it uses only the Python standard library (`random`, `os`, `sys`, `datetime`). There is nothing to `pip install`.

## Install

```bash
git clone https://github.com/Mkrolick/operant-league.git
cd operant-league
```

That's it — no dependencies to install.

## Run

Directly with Python:

```bash
python3 main.py
```

Or via the provided wrapper script:

```bash
./run.sh
```

### Optional flags

- `--show-status` — enable the "Tasks Completed: X / Y" readout (option 2, and after each completed task). Without this flag your progress is hidden, keeping the "variable ratio" suspense.
- `--target-changeable` — allow menu option 3 to manually override the current target.

Example:

```bash
python3 main.py --show-status --target-changeable
```

### Expected behavior

```
Welcome to the Task-Reward Tracker!
Your current target is 4 tasks before you can play a League match.

Choose an option:
1) Mark a task as completed
2) Check current status
3) Reset the target manually (if needed)
4) Exit

Enter your choice (1-4):
```

Enter `1` each time you finish a real task. When your completed count reaches the hidden target you'll see:

```
*** Congratulations! You've earned a League of Legends match! ***
```

...at which point it asks you to type `play` to confirm, then rolls a fresh random target. Enter `4` to exit.

A `task_log.txt` file records every action with a timestamp; it is created automatically on first run if it doesn't exist.

## Configuring the task range

By default the target is a random integer between **2 and 6** tasks.

> **Known issue — the `--min-tasks` / `--max-tasks` flags are currently ignored.**
> The program parses `--min-tasks=N` and `--max-tasks=N` and even validates them, but the actual target is always rolled from the module-level `MIN_TASKS` and `MAX_TASKS` constants — the parsed values are never used. Passing these flags therefore has **no effect** on the range.
>
> To actually change the range, edit the constants near the top of `main.py`:
>
> ```python
> MIN_TASKS = 2   # minimum number of tasks
> MAX_TASKS = 6   # maximum number of tasks
> ```

## License

No license file is included, so all rights are reserved by the author by default.
