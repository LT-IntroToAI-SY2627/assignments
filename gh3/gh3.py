# gh3.py
# GH-3: Loops & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: Torin Lee

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
assert sum_list([1, 2, 3]) == 6
assert sum_list([-1, 0, 1]) == 0

# Problem 2
def count_above(numbers, threshold):
    total = 0
    for num in numbers:
        if num > threshold:
            total += 1
    return total
assert count_above([1, 2, 3], 2) == 1
assert count_above([1, 2, 3], 3) == 0
# Problem 3
def categorize_scores(scores):
    categsories = []
    for score in scores:
        if score >= 90:
            categories.append("A")
        elif score >= 80:
            categories.append("B")
        elif score >= 70:
            categories.append("C")
        elif score >= 60:
            categories.append("D")
        else:
            categories.append("F")
    return categories


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    for i in range(len(lst) // 2):
        temp = lst[i]
        lst[i] = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = temp
    return lst

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    vowels = set("aeiou")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
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
