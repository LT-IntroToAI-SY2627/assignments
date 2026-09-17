# gh3.py
# GH-3: Loops & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: Jackson Knight

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def sum_list(numbers):
    s = 0

    for num in numbers:
        s = s + num
    return s

assert sum_list([1, 2, 3]) == 6


# Problem 2
def count_above(numbers, threshold):
    count = 0

    for num in numbers:
        if num > threshold:
            count = count + 1
    return count

assert count_above([1, 2, 3, 4], 2) == 2
            
# Problem 3
def categorize_scores(scores):
    categorized_list = []
    for score in scores:
        if score >= 90:
            categorized_list.append("A")
        elif score >= 80:
            categorized_list.append("B")
        elif score >= 70:
            categorized_list.append("C")
        elif score >= 60:
            categorized_list.append("D")
        elif score < 60:
            categorized_list.append("F")
        else:
            categorized_list.append("Invalid Score")

    return categorized_list


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    reversed_list = []

    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list


assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    count = 0
    for char in s:
        if char == "a" or char == "A":
            count += 1
        elif char == "e" or char == "E":
            count += 1
        elif char == "i" or char == "I":
            count += 1
        elif char == "o" or char == "O":
            count += 1
        elif char == "u" or char == "U":
            count += 1
        else:
            count += 0
    return count

assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0


# Problem 6
def fizzbuzz(n):
    nList = []
    x = 1
    while x <= n:
        nList.append(x)
        x += 1

    for num in nList:
        if num % 3 == 0 and num % 5 == 0:
            num = "FizzBuzz"
        elif num % 3 == 0:
            num = "Fizz"
        elif num % 5 == 0:
            num = "Buzz"
        else:
            num = num

    return nList

assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
