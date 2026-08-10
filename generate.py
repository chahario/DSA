#!/usr/bin/env python3
"""
DSA Tracker generator.
Reads plan.md (your study plan) and creates:
  problems/LC<id>/solution.py   (stub, never overwrites your work)
  problems/LC<id>/notes.md      (stub, never overwrites your work)
  README.md                     (master progress tracker, regenerated each run)

Run it again any time you edit plan.md — it re-links everything and
only creates missing files, so your solutions/notes are safe.
"""
import os, re, sys

PLAN = "plan.md"
PROB_DIR = "problems"

day_re  = re.compile(r'^##\s+Day\s+(\d+)\s*\((.*?)\)\s*[—-]\s*(.*)$')
# LC id | name | topic | difficulty | companies(optional/lenient)
prob_re = re.compile(
    r'^\s*[-*]\s+\*\*LC(\d+)\*\*\s*[—-]\s*(.*?)\s*\|\s*\*\*(.*?)\*\*\s*\|\s*\*\*(.*?)\*\*'
)

def slug(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]

def parse(path):
    days = []
    cur = None
    for line in open(path, encoding="utf-8"):
        m = day_re.match(line)
        if m:
            cur = {"num": int(m.group(1)), "date": m.group(2).strip(),
                   "title": m.group(3).strip(), "probs": []}
            days.append(cur)
            continue
        m = prob_re.match(line)
        if m and cur is not None:
            cur["probs"].append({
                "id": m.group(1),
                "name": m.group(2).strip(),
                "topic": m.group(3).strip(),
                "diff": m.group(4).strip(),
            })
    return days

def main():
    if not os.path.exists(PLAN):
        sys.exit(f"Missing {PLAN}. Save your study plan as {PLAN} next to this script.")
    days = parse(PLAN)
    total_lines = sum(len(d["probs"]) for d in days)

    # unique problems -> stub folders
    uniq = {}
    for d in days:
        for p in d["probs"]:
            uniq.setdefault(p["id"], p)

    os.makedirs(PROB_DIR, exist_ok=True)
    created = 0
    for pid, p in uniq.items():
        folder = os.path.join(PROB_DIR, f"LC{pid}_{slug(p['name'])}")
        os.makedirs(folder, exist_ok=True)
        sol = os.path.join(folder, "Solution.java")
        note = os.path.join(folder, "notes.md")
        if not os.path.exists(sol):
            open(sol, "w", encoding="utf-8").write(
                f"// LC{pid} — {p['name']}\n"
                f"// Topic: {p['topic']} | Difficulty: {p['diff']}\n"
                f"// https://leetcode.com/problems/{slug(p['name'])}/\n\n"
                f"class Solution {{\n\n}}\n")
            created += 1
        if not os.path.exists(note):
            open(note, "w", encoding="utf-8").write(
                f"# LC{pid} — {p['name']}\n\n"
                f"**Topic:** {p['topic']}  \n**Difficulty:** {p['diff']}\n\n"
                f"## Idea\n\n## Approach\n\n## Complexity\n- Time: \n- Space: \n\n"
                f"## Pitfalls / edge cases\n\n## Revisit?\n- [ ] Need another pass\n")
            created += 1

    # folder lookup for links
    link = {pid: f"LC{pid}_{slug(p['name'])}" for pid, p in uniq.items()}

    # README
    out = ["# DSA Tracker\n",
           f"`{len(uniq)}` unique problems across `{len(days)}` days "
           f"({total_lines} scheduled slots). Tick a box when a problem is solved.\n",
           "> Edit `plan.md` and rerun `python generate.py` to refresh this file.\n"]
    for d in days:
        out.append(f"\n## Day {d['num']} — {d['title']}\n")
        out.append("| ✓ | Problem | Topic | Diff | Solution | Notes |")
        out.append("|---|---------|-------|------|----------|-------|")
        for p in d["probs"]:
            f = link[p["id"]]
            out.append(
                f"| [ ] | LC{p['id']} {p['name']} | {p['topic']} | {p['diff']} "
                f"| [code]({PROB_DIR}/{f}/Solution.java) | [notes]({PROB_DIR}/{f}/notes.md) |")
    open("README.md", "w", encoding="utf-8").write("\n".join(out) + "\n")

    print(f"Days parsed:        {len(days)}")
    print(f"Scheduled slots:    {total_lines}")
    print(f"Unique problems:    {len(uniq)}")
    print(f"New stub files:     {created}")
    print("Wrote README.md")

if __name__ == "__main__":
    main()
