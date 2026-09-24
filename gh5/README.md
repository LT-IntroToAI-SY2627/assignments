# GH-5: String Manipulation + First InfoBot Contribution

**Introduction to AI | Lane Tech College Prep**  
**Unit 1 — Python Basics & GitHub**  
**Worth: 10 points**

---

## Overview

This assignment has two parts. First you will complete string manipulation problems in the `assignments` repo as usual. Then you will make your first contribution to the Lane Tech Info Bot — the shared class project you will be building all year.

**Python concepts:** String methods, indexing, splitting, formatting  
**GitHub concept:** Contributing to a shared repo, opening a pull request, resolving merge conflicts

---

## Scoring

| Task | Points |
|---|---|
| Problem 3 passing | 2 pts |
| Problem 4 passing | 2 pts |
| In-class problems completed | 2 pts |
| InfoBot contribution submitted as PR | 4 pts |
| **Minimum for any submission** | **5 pts** |
| **Total** | **10 pts** |

---

## Part 1 — String Manipulation (assignments repo)

### Setup

**Step 1 — Fetch and pull from main:**
```bash
git fetch origin
git checkout main
git pull origin main
```

**Step 2 — Create your personal branch:**
```bash
git checkout -b gh5-firstnamelastinitial
```

**Step 3 — Verify you have the assignment files:**
```bash
ls
```
You should see a `gh5/` folder. If you do not, go back to Step 1 and try again.

**Step 4 — Open `gh5.py` in VS Code and work through the problems.**

---

### In-Class Problems

#### Problem 1 — `make_greeting(name)`
Takes a name and returns a friendly greeting string for the Info Bot to use.

```
make_greeting("Alex")       ->  "Hey Alex, welcome to the Lane Tech Info Bot!"
make_greeting("Mr. Berg")   ->  "Hey Mr. Berg, welcome to the Lane Tech Info Bot!"
```

#### Problem 2 — `clean_input(text)`
Takes a string of user input and returns it stripped of leading/trailing whitespace and converted to lowercase. This is how the bot will process questions before trying to answer them.

```
clean_input("  What clubs are there?  ")  ->  "what clubs are there?"
clean_input("HELLO")                       ->  "hello"
```

---

### Independent Problems

Read the descriptions below. Open `gh5.py` and complete each function. The asserts in the file will tell you if your solution is correct.

#### Problem 3 — `count_words(text)`
Takes a string and returns the number of words in it. An empty string should return 0.

#### Problem 4 — `initials(full_name)`
Takes a full name as a string and returns the initials with periods after each letter.

---

### Submitting Part 1

```bash
git add .
git commit -m "Complete gh5 string manipulation"
git push origin gh5-firstnamelastinitial
```

Check the **Actions** tab on GitHub to see your autograder results.

---

## Part 2 — Lane Tech Info Bot Contribution

This is your first contribution to the shared class project. You will add a function to `contributors.py` in the `LT-InfoBot-SY2627` repository.

### Setup

**Step 1 — Clone the InfoBot repo if you haven't already:**
```bash
git clone https://github.com/LT-IntroToAI-SY2627/LT-InfoBot-SY2627.git
cd LT-InfoBot-SY2627
```

**Step 2 — Fetch and switch to dev:**
```bash
git fetch origin
git checkout dev
git pull origin dev
```

**Step 3 — Create your personal feature branch:**
```bash
git checkout -b contrib-firstnamelastinitial
```

### Your Contribution

Open `contributors.py` and add your function following this exact format:

```python
def greet_firstnamelastinitial():
    return {
        "name": "Your Full Name",
        "fun_fact": "One fun fact about yourself"
    }
```

**Example:**
```python
def greet_alexj():
    return {
        "name": "Alex Johnson",
        "fun_fact": "I have two dogs and love hiking"
    }
```

> **Important:** Do not edit anyone else's function — only add your own.

### Submitting Part 2

```bash
git add .
git commit -m "Add greet_firstnamelastinitial to contributors"
git push origin contrib-firstnamelastinitial
```

Then open a **Pull Request** on GitHub:
- Go to the `LT-InfoBot-SY2627` repo
- Click **Compare & pull request**
- Set the base branch to `dev`
- Title your PR: `GH-5 Contribution: [Your Name]`
- Submit and wait — Mr. Berg will merge these together in class

> **Note:** When multiple students edit the same file, Git may flag a merge conflict. Mr. Berg will walk through resolving these together as a class — this is a normal part of collaborative development.

---

## Checklist Before You Submit

- [ ] Branch `gh5-firstnamelastinitial` pushed to assignments repo
- [ ] Problems 3 and 4 passing in the autograder
- [ ] In-class problems completed
- [ ] `greet_firstnamelastinitial()` added to `contributors.py`
- [ ] PR opened targeting `dev` in `LT-InfoBot-SY2627`
- [ ] PR title is `GH-5 Contribution: [Your Name]`

---

*Questions? Ask Mr. Berg or check the [GitHub Workflow Guide](../../profile/GITHUB_WORKFLOW.md).*
