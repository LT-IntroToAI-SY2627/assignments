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
    grades = []
    for i in scores:
        if i >= 90:
            grades.append("A")
        elif i >= 80:
            grades.append("B")
        elif i >= 70:
            grades.append("C")
        elif i >= 60:
            grades.append("D")
        else:
            grades.append("F")
    return grades


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    list = []
    i = len(lst) - 1
    for num in range(len(lst)):
        list.append(lst[i])
        i -= 1
    return list

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    list = []
    for i in range(n):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            list.append("FizzBuzz")
        elif (i + 1) % 3 == 0:
            list.append("Fizz")
        elif (i + 1) % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i + 1)
    return list

assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
