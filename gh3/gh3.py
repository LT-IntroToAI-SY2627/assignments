# gh3.py
# GH-3: Loops & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: [Ashton Boeke]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1

def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
assert sum_list([1, 2, 3, 4, 5]) == 15
assert sum_list([]) == 0

# Problem 2
def count_above(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count
assert count_above([1, 2, 3, 4, 5], 2) == 3
assert count_above([1, 2, 3], 10) == 0

# Problem 3
def categorize_scores(scores):
    grades = []
    for score in scores:
        if score >= 90:
            grades.append("A")
        elif score >= 80:
            grades.append("B")
        elif score >= 70:
            grades.append("C")
        elif score >= 60:
            grades.append("D")
        else:
            grades.append("F")
    return grades
assert categorize_scores([95, 83, 72, 55]) == ["A", "B", "C", "F"]
assert categorize_scores([100, 60]) == ["A", "D"]

# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []


# Problem 5
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
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
