# Setup (2 minutes)

## Option A — just push it (fastest)
Everything is already generated. From this folder:

    git init
    git add .
    git commit -m "DSA tracker: 50-day plan"
    # make an empty repo on github.com, then:
    git remote add origin https://github.com/<you>/dsa-tracker.git
    git push -u origin main

Open the repo on GitHub — the README is your live tracker. Change `[ ]`
to `[x]` as you solve each problem (GitHub renders them as checkboxes).

## Option B — regenerate anytime
Edit `plan.md`, then:

    python3 generate.py

It relinks the README and creates folders for any NEW problems.
It NEVER overwrites a Solution.java or notes.md you've already written.

## Daily flow
1. Solve a problem, paste code into `problems/LCxxx_.../Solution.java`
2. Jot the idea in `problems/LCxxx_.../notes.md`
3. Tick the box in README.md, commit, push
