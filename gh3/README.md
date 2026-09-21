# GH-3: Loops & Conditionals

**Introduction to AI | Lane Tech College Prep**  
**Unit 1 — Python Basics & GitHub**  
**Worth: 10 points**

---

## Overview

In this assignment you will practice loops and conditionals. The first three problems will be completed in class together. The last three you will complete independently.

**Python concepts:** for loops, while loops, conditionals, list iteration  
**GitHub concept:** Multiple commits on one branch — commit after each problem, not just at the end

---

## Scoring

| Task | Points |
|---|---|
| Problem 4 passing | 2 pts |
| Problem 5 passing | 2 pts |
| Problem 6 passing | 2 pts |
| In-class problems completed | 2 pts |
| Commit history shows multiple commits | 2 pts |
| **Minimum for any submission** | **5 pts** |
| **Total** | **10 pts** |

---

## Setup

```bash
git fetch origin
git checkout main
git pull origin main
git checkout -b gh3-firstnamelastinitial
```

Open `gh3.py` in VS Code and work through the problems.

> **Commit after each problem** — your commit history is part of your grade this time.  
> Example commit messages:  
> ✅ `Complete sum_list`  
> ✅ `Complete count_above`  
> ❌ `done` `all problems` `finished`

---

## In-Class Problems

### Problem 1 — `sum_list(numbers)`
Takes a list of numbers and returns the total sum of all items in the list. Do not use the built-in `sum()` function — use a loop.

```python
sum_list([1, 2, 3, 4, 5])  ->  15
sum_list([10, 20])          ->  30
sum_list([])                ->  0
```

### Problem 2 — `count_above(numbers, threshold)`
Takes a list of numbers and a threshold value. Returns how many numbers in the list are strictly greater than the threshold.

```
count_above([1, 5, 3, 8, 2], 4)  ->  2
count_above([10, 20, 30], 25)     ->  1
count_above([1, 2, 3], 10)        ->  0
```

### Problem 3 — `categorize_scores(scores)`
Takes a list of numeric scores and returns a new list where each score is replaced by its letter grade.

```
90 and above  ->  "A"
80 to 89      ->  "B"
70 to 79      ->  "C"
60 to 69      ->  "D"
below 60      ->  "F"
```

```
categorize_scores([95, 83, 72, 55])  ->  ["A", "B", "C", "F"]
categorize_scores([100, 60])         ->  ["A", "D"]
```

---

## Independent Problems

Read the descriptions below. Open `gh3.py` and complete each function. The asserts in the file will tell you if your solution is correct.

### Problem 4 — `reverse_list(lst)`
Takes a list and returns a new list with the items in reverse order. Do not use the built-in `reverse()` or slicing shortcut — use a loop.

### Problem 5 — `count_vowels(s)`
Takes a string and returns the number of vowels in it. Vowels are a, e, i, o, u. Your function should work for both uppercase and lowercase letters.

### Problem 6 — `fizzbuzz(n)`
Takes a number `n` and returns a list of values from 1 to n where:
- Multiples of 3 are replaced with `"Fizz"`
- Multiples of 5 are replaced with `"Buzz"`
- Multiples of both 3 and 5 are replaced with `"FizzBuzz"`
- All other numbers stay as integers

---

## Submitting

```bash
git add .
git commit -m "Complete gh3 independent problems"
git push origin gh3-firstnamelastinitial
```

Check the **Actions** tab on GitHub to see your autograder results.

---

## Checklist Before You Submit

- [ ] Branch is named `gh3-firstnamelastinitial`
- [ ] In-class problems completed
- [ ] Problems 4, 5, and 6 passing
- [ ] Multiple commits in your history — one per problem
- [ ] Pushed to GitHub

---

*Questions? Ask Mr. Berg or check the [GitHub Workflow Guide](../../profile/GITHUB_WORKFLOW.md).*
