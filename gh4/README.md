# GH-4: Lists

**Introduction to AI | Lane Tech College Prep**  
**Unit 1 — Python Basics & GitHub**  
**Worth: 10 points**

---

## Overview

In this assignment you will practice working with lists — one of the most important data structures in Python. The first three problems will be completed in class together. The last three you will complete independently.

**Python concepts:** Lists, indexing, looping, slicing  
**GitHub concept:** Pushing your own branch — make sure you are on your personal branch before you push

---

## Scoring

| Task | Points |
|---|---|
| Problem 4 passing | 2 pts |
| Problem 5 passing | 2 pts |
| Problem 6 passing | 2 pts |
| In-class problems completed | 2 pts |
| Multiple meaningful commits | 2 pts |
| **Minimum for any submission** | **5 pts** |
| **Total** | **10 pts** |

---

## Setup

**Step 1 — Fetch all branches so Git knows about the latest assignments:**
```bash
git fetch origin
```

**Step 2 — Switch to main and pull the latest files:**
```bash
git checkout main
git pull origin main
```

**Step 3 — Create your personal branch:**
```bash
git checkout -b gh4-firstnamelastinitial
```

**Step 4 — Verify you have the assignment files:**
```bash
ls
```
You should see a `gh4/` folder. If you do not, go back to Step 1 and try again.

**Step 5 — Open `gh4.py` in VS Code and work through the problems.**

---

## In-Class Problems

### Problem 1 — `get_first(lst)`
Takes a list and returns the first item using indexing. Do not use any built-in methods.

```
get_first([10, 20, 30])  ->  10
get_first(["a", "b"])    ->  "a"
```

### Problem 2 — `list_min(lst)`
Takes a list of numbers and returns the smallest one. Do not use the built-in `min()` function — use a loop.

```
list_min([3, 1, 4, 1, 5])  ->  1
list_min([10, 20, 5])      ->  5
list_min([7])              ->  7
```

### Problem 3 — `sum_positive(lst)`
Takes a list of numbers and returns the sum of only the positive numbers. Negative numbers and zero are ignored.

```
sum_positive([1, -2, 3, -4, 5])  ->  9
sum_positive([-1, -2, -3])       ->  0
sum_positive([10, 20, 30])       ->  60
```

---

## Independent Problems

Read the descriptions below. Open `gh4.py` and complete each function. The asserts in the file will tell you if your solution is correct.

### Problem 4 — `remove_duplicates(lst)`
Takes a list and returns a new list with duplicate values removed, keeping only the first occurrence of each item. Maintain the original order.

### Problem 5 — `every_other(lst)`
Takes a list and returns every other item starting from the first, using slicing.

### Problem 6 — `is_sorted(lst)`
Takes a list and returns `True` if the items are in ascending order, `False` if they are not. An empty list should return `True`.

---

## Submitting

When you are done, commit and push:

```bash
git add .
git commit -m "Complete gh4 lists assignment"
git push origin gh4-firstnamelastinitial
```

> **Commit after each problem** — your commit history is part of your grade.  
> ✅ `Complete get_first and list_min`  
> ✅ `Complete sum_positive`  
> ❌ `done` `finished` `stuff`

Check the **Actions** tab on GitHub to see your autograder results.

---

## Checklist Before You Submit

- [ ] Branch is named `gh4-firstnamelastinitial`
- [ ] In-class problems completed
- [ ] Problems 4, 5, and 6 passing
- [ ] Multiple commits in your history
- [ ] Pushed to GitHub

---

*Questions? Ask Mr. Berg or check the [GitHub Workflow Guide](../../profile/GITHUB_WORKFLOW.md).*
