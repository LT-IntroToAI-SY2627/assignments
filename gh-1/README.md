# GH-1: GitHub Setup

**Introduction to AI | Lane Tech College Prep**  
**Unit 1 — Python Basics & GitHub**  
**Worth: 10 points**

---

## Overview

In this assignment you will set up your GitHub environment, learn the basic workflow you will use all year, and make your first contribution to the class repository. By the end you will have cloned the repo, created your own branch, and submitted a pull request.

**GitHub skill:** Clone, branch, commit, push, open a PR

---

## Scoring

| Task | Points |
|---|---|
| Branch created with correct naming convention | 2 pts |
| Name added to `roster.md` | 2 pts |
| Meaningful commit message and PR opened correctly | 2 pts |
| Your Contribution section completed | 4 pts |
| **Minimum for any submission** | **5 pts** |
| **Total** | **10 pts** |

---

## Walkthrough

Follow these steps carefully. We will use **Alex Johnson** as our example student.

---

### Step 1 — Accept the invitation

Check your email for an invitation to join the `LT-IntroToAI-SY2627` GitHub organization. Accept it before continuing.

---

### Step 2 — Clone the repository

Open a terminal on your VM and run:

```bash
git clone https://github.com/LT-IntroToAI-SY2627/assignments.git
```

Then navigate into the repo:

```bash
cd assignments
```

---

### Step 3 — Switch to the GH-1 branch

Mr. Berg has already created a `gh1` branch with starter files. Switch to it:

```bash
git checkout gh1
git pull origin gh1
```

---

### Step 4 — Create your personal branch

Create a new branch using the naming convention `gh1-firstnamelastinitial`. Alex would run:

```bash
git checkout -b gh1-alexj
```

> **Naming convention:** Use your first name and last initial, all lowercase, no spaces.  
> Examples: `gh1-alexj`, `gh1-mariac`, `gh1-jamesw`

---

### Step 5 — Add your name to roster.md

Open `roster.md` in VS Code. Mr. Berg has already added everyone's name as a placeholder. Find your line and replace the placeholder with your full name.

Before:
```
# Class Roster

- [Student 1]
- [Student 2]
- Alex Johnson    ← Alex finds their line and fills it in
- [Student 4]
```

After:
```
# Class Roster

- [Student 1]
- [Student 2]
- Alex Johnson
- [Student 4]
```

Only edit your own line — leave everyone else's placeholders alone. Save the file.

---

### Step 6 — Commit and push

Stage your changes, write a commit message, and push your branch:

```bash
git add .
git commit -m "Add [Your Name] to roster"
git push origin gh1-alexj
```

> **Good commit messages** are short and present tense. Describe what you did:  
> ✅ `Add Alex Johnson to roster`  
> ❌ `stuff` `changes` `I added my name`

---

### Step 7 — Open a Pull Request

1. Go to [github.com/LT-IntroToAI-SY2627/assignments](https://github.com/LT-IntroToAI-SY2627/assignments)
2. Click **Compare & pull request**
3. Make sure the base branch is set to `gh1` — **not main**
4. Title your PR: `GH-1: [Your Name]`
5. Add a short description of what you did
6. Click **Create pull request**

---

## Your Contribution

Now that you have completed the walkthrough, do the following on your own — **without step-by-step instructions.**

In the `gh1` folder, create a new file called `fun_fact_yourfirstnamelastinitial.md` (example: `fun_fact_alexj.md`). Inside it, write:

- Your name
- One fun fact about yourself
- One thing you hope to build or learn this year

Commit the file to your branch with a meaningful commit message and make sure it is included in your pull request before you submit.

> **Example file name:** `fun_fact_alexj.md`  
> **Example commit message:** `Add fun fact file for alexj`

---

## Checklist Before You Submit

- [ ] Branch is named `gh1-firstnamelastinitial`
- [ ] Your name is added to `roster.md`
- [ ] `fun_fact_yourfirstnamelastinitial.md` is created and filled out
- [ ] All changes are committed with a meaningful message
- [ ] Pull request is open and targeting the `gh1` branch
- [ ] PR title is `GH-1: [Your Name]`

---

*Questions? Ask Mr. Berg or check the [GitHub Workflow Guide](../../profile/GITHUB_WORKFLOW.md).*
