# gh3.py
# GH-3: Loops & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: [Your Name Here]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
assert sum_list([1, 2, 3, 4, 5]) == 15

# Problem 2
def count_above(numbers, threshold):
    pass

# Problem 3
def categorize_scores(scores):
    pass


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    pass

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    pass

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    pass

assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
