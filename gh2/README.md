# GH-2: Functions & Conditionals

**Introduction to AI | Lane Tech College Prep**  
**Unit 1 — Python Basics & GitHub**  
**Worth: 10 points**

---

## Overview

In this assignment you will write Python functions using parameters, return values, and conditionals. When you push your branch, GitHub will automatically run tests and report pass/fail on each problem.

**Python concepts:** Functions, parameters, return values, conditionals  
**GitHub concept:** Writing meaningful commit messages — your commit message is how you communicate what you did

---

## Scoring

| Task | Points |
|---|---|
| Problem 1 passing | 3 pts |
| Problem 2 passing | 3 pts |
| Your Contribution completed | 4 pts |
| **Minimum for any submission** | **5 pts** |
| **Total** | **10 pts** |

---

## Setup

**Step 1 — Pull the latest from main:**
```bash
git fetch origin
git checkout main
git pull origin main
```

**Step 2 — Create your personal branch:**
```bash
git checkout -b gh2-firstnamelastinitial
```

**Step 3 — Open `gh2.py` in VS Code and complete the problems.**

---

## Problems

Open `gh2.py` — the function stubs are already there. Replace each `pass` with your solution.

### Problem 1 — `multiply(a, b)`
Write a function that takes two numbers and returns their product.

```
multiply(3, 4)   ->  12
multiply(5, 0)   ->  0
multiply(2, 2)   ->  4
```

### Problem 2 — `classify_temp(temp)`
Write a function that takes a temperature in Fahrenheit and returns a string:

```
90 or above  ->  "hot"
70 to 89     ->  "warm"
50 to 69     ->  "cool"
below 50     ->  "cold"
```

```
classify_temp(95)  ->  "hot"
classify_temp(75)  ->  "warm"
classify_temp(55)  ->  "cool"
classify_temp(30)  ->  "cold"
```

### Your Contribution
Write your own original function at the bottom of `gh2.py`. It must:
- Have at least one parameter
- Use a conditional (if/elif/else)
- Return a value
- Include at least 2 asserts that test it

---

## Submitting

When you are done, commit and push:

```bash
git add .
git commit -m "Complete GH-2 functions and conditionals"
git push origin gh2-firstnamelastinitial
```

> **Write a meaningful commit message** — describe what you actually did.  
> ✅ `Complete GH-2 functions and conditionals`  
> ✅ `Add multiply, classify_temp, and custom function`  
> ❌ `done` `stuff` `idk`

After you push, click the **Actions** tab in the repo on GitHub to see your test results. A green checkmark means passing, a red X means something needs fixing.

---

## Checklist Before You Submit

- [ ] Branch is named `gh2-firstnamelastinitial`
- [ ] `multiply()` is complete and passing
- [ ] `classify_temp()` is complete and passing
- [ ] Your Contribution function is written with at least 2 asserts
- [ ] Commit message is meaningful
- [ ] Pushed to GitHub

---

*Questions? Ask Mr. Berg or check the [GitHub Workflow Guide](../../profile/GITHUB_WORKFLOW.md).*
