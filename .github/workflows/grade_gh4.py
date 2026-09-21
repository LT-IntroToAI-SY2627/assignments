#!/usr/bin/env python3
# grade_gh4.py
# Local grading script for GH-4
# Run from inside your assignments folder:
#   python grade_gh4.py

import subprocess
import importlib.util
import sys
import os
import tempfile

# =============================================================================
# TEST CASES
# =============================================================================

def run_tests(module):
    results = []

    # --- Problem 1: get_first ---
    p1_tests = [
        ("get_first([10, 20, 30])", lambda: module.get_first([10, 20, 30]), 10),
        ("get_first(['a', 'b'])",   lambda: module.get_first(["a", "b"]), "a"),
        ("get_first([99])",          lambda: module.get_first([99]), 99),
    ]
    results.append(("Problem 1 — get_first", p1_tests))

    # --- Problem 2: list_min ---
    p2_tests = [
        ("list_min([3, 1, 4, 1, 5])", lambda: module.list_min([3, 1, 4, 1, 5]), 1),
        ("list_min([10, 20, 5])",      lambda: module.list_min([10, 20, 5]), 5),
        ("list_min([7])",              lambda: module.list_min([7]), 7),
    ]
    results.append(("Problem 2 — list_min", p2_tests))

    # --- Problem 3: sum_positive ---
    p3_tests = [
        ("sum_positive([1, -2, 3, -4, 5])", lambda: module.sum_positive([1, -2, 3, -4, 5]), 9),
        ("sum_positive([-1, -2, -3])",       lambda: module.sum_positive([-1, -2, -3]), 0),
        ("sum_positive([10, 20, 30])",        lambda: module.sum_positive([10, 20, 30]), 60),
    ]
    results.append(("Problem 3 — sum_positive", p3_tests))

    # --- Problem 4: remove_duplicates ---
    p4_tests = [
        ("remove_duplicates([1, 2, 2, 3, 3, 3])", lambda: module.remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3]),
        ("remove_duplicates([1, 1, 1])",            lambda: module.remove_duplicates([1, 1, 1]), [1]),
        ("remove_duplicates([])",                   lambda: module.remove_duplicates([]), []),
    ]
    results.append(("Problem 4 — remove_duplicates", p4_tests))

    # --- Problem 5: every_other ---
    p5_tests = [
        ("every_other([1, 2, 3, 4, 5])", lambda: module.every_other([1, 2, 3, 4, 5]), [1, 3, 5]),
        ("every_other([10, 20, 30])",     lambda: module.every_other([10, 20, 30]), [10, 30]),
        ("every_other([])",               lambda: module.every_other([]), []),
    ]
    results.append(("Problem 5 — every_other", p5_tests))

    # --- Problem 6: is_sorted ---
    p6_tests = [
        ("is_sorted([1, 2, 3, 4, 5])", lambda: module.is_sorted([1, 2, 3, 4, 5]), True),
        ("is_sorted([1, 3, 2, 4, 5])", lambda: module.is_sorted([1, 3, 2, 4, 5]), False),
        ("is_sorted([])",               lambda: module.is_sorted([]), True),
    ]
    results.append(("Problem 6 — is_sorted", p6_tests))

    return results

# =============================================================================
# GRADING ENGINE
# =============================================================================

def get_student_branches():
    result = subprocess.run(
        ["git", "branch", "-r"],
        capture_output=True, text=True
    )
    branches = []
    for line in result.stdout.splitlines():
        branch = line.strip().replace("origin/", "")
        if branch.startswith("gh4-"):
            branches.append(branch)
    return sorted(branches)

def load_student_module(branch):
    try:
        result = subprocess.run(
            ["git", "show", f"origin/{branch}:gh4/gh4.py"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            return None, "gh4.py not found on branch"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(result.stdout)
            tmp_path = f.name

        spec = importlib.util.spec_from_file_location("gh4_student", tmp_path)
        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
        except AssertionError as e:
            os.unlink(tmp_path)
            return None, f"AssertionError on import: {e}"
        except Exception as e:
            os.unlink(tmp_path)
            return None, f"Error on import: {e}"

        os.unlink(tmp_path)
        return module, None

    except Exception as e:
        return None, str(e)

def grade_student(branch, module):
    test_groups = run_tests(module)
    print(f"\n  {'─' * 50}")

    total_pass = 0
    total_fail = 0

    for problem_name, tests in test_groups:
        passes = []
        fails = []

        for label, fn, expected in tests:
            try:
                actual = fn()
                if actual == expected:
                    passes.append(label)
                    total_pass += 1
                else:
                    fails.append((label, expected, actual))
                    total_fail += 1
            except Exception as e:
                fails.append((label, expected, f"ERROR: {e}"))
                total_fail += 1

        status = "✅ PASS" if not fails else "❌ FAIL"
        print(f"  {status}  {problem_name}")

        for label, expected, actual in fails:
            print(f"         ✗ {label}")
            print(f"           expected: {expected}")
            print(f"           got:      {actual}")

    return total_pass, total_fail

# =============================================================================
# MAIN
# =============================================================================

def main():
    print("\n" + "=" * 60)
    print("  GH-4 GRADING SUMMARY")
    print("=" * 60)

    print("\nFetching latest branches from GitHub...")
    subprocess.run(["git", "fetch", "origin"], capture_output=True)

    branches = get_student_branches()

    if not branches:
        print("\nNo gh4-* branches found. Make sure you have fetched from origin.")
        return

    print(f"Found {len(branches)} student branch(es): {', '.join(branches)}\n")

    summary = []

    for branch in branches:
        student = branch.replace("gh4-", "")
        print(f"\n{'=' * 60}")
        print(f"  STUDENT: {student.upper()}  ({branch})")

        module, error = load_student_module(branch)

        if error:
            print(f"\n  ⚠️  Could not load gh4.py — {error}")
            summary.append((student, "LOAD ERROR", 0, 0))
            continue

        total_pass, total_fail = grade_student(branch, module)
        summary.append((student, "graded", total_pass, total_fail))

    # Final summary table
    print("\n\n" + "=" * 60)
    print("  FINAL SUMMARY")
    print("=" * 60)
    print(f"  {'Student':<20} {'Pass':<8} {'Fail':<8} {'Status'}")
    print(f"  {'─'*20} {'─'*8} {'─'*8} {'─'*10}")

    for student, status, passes, fails in summary:
        if status == "LOAD ERROR":
            print(f"  {student:<20} {'—':<8} {'—':<8} ⚠️  Load Error")
        else:
            emoji = "✅" if fails == 0 else "❌"
            print(f"  {student:<20} {passes:<8} {fails:<8} {emoji}")

    print()

if __name__ == "__main__":
    main()
