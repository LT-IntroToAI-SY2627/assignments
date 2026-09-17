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
assert sum_list([])==0
# Problem 2
def count_above(numbers, threshold):
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count
assert count_above([1, 2, 3, 4], 2) == 2
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
assert categorize_scores([95, 85, 75, 65, 55]) == {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list


assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
