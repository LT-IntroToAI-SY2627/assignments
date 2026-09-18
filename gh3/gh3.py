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
    s = 0
    for num in numbers:
        s += num
    return s
assert sum_list([1, 2, 3]) == 6
assert sum_list([]) == 0

# Problem 2
def count_above(numbers, threshold=6):
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count

assert count_above([1, 2, 3, 4, 5], 3) == 0
assert count_above([1, 2, 3, 4, 5], 10) == 1


# Problem 3
def categorize_scores(scores):
    categories = []
    for score in scores:
        if score >= 90:
            categories.append("A")
        if 79.5 <= score < 89.4:
            categories.append("B")
        if 69.5 <= score < 79.4:
            categories.append("C")
        if 59.5 <= score < 69.4:
            categories.append("D")
        else:
            categories.append("F")
    return categories

assert categorize_scores([95, 85, 75, 65, 55]) == ["A", "B", "C", "D", "F"]
assert categorize_scores([100, 90, 80, 70, 60]) == ["A", "A", "B", "C", "D"]

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
