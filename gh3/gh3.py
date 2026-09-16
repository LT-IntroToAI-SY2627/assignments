# gh3.py
# GH-3: Loops & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: Simona Arsic

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

# Problem 2
def count_above(numbers, threshold):
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count

# Problem 3
def categorize_scores(scores):
    categories = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        if score >= 90:
            categories["A"] += 1
        elif score >= 80:
            categories["B"] += 1
        elif score >= 70:
            categories["C"] += 1
        elif score >= 60:
            categories["D"] += 1
        else:
            categories["F"] += 1
    return categories


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    revered = []
    for item in lst:
        revered.insert(0, item)
    return revered

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    newlist = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            newlist.append("FizzBuzz")
        elif num % 3 == 0:
            newlist.append("Fizz")
        elif num % 5 == 0:
            newlist.append("Buzz")
        else:
            newlist.append(num)
    return newlist

assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
