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
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count
assert count_above([1, 5, 3, 8, 2], 4) == 2


# Problem 3
def categorize_scores(scores):
    grades = [0]

    for score in scores:
        if score >= 90:
            score.append("A")
        elif score >= 80:
            score.append("B")
        elif score >= 70:
            score.append("C")
        elif score >= 60:
            score.append("D")
        else:
            score.append("F")

    return grades

assert categorize_scores([95, 83, 72, 55]) == ["A", "B", "C", "F"]
assert categorize_scores([25, 85, 79.9, 65]) == ["F", "B", "C", "D"])


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def reverse_list(lst):
    reversed_list = []

    for l in list:
        reversed_list.insert(0, l)

    return reversed_list

assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([5]) == [5]
assert reverse_list([]) == []
assert revere_list([15, 21, 80, 43]) == [43, 80, 21, 15]

# Problem 5
def count_vowels(s):
    count = 0

    for letter in s:
        if letter.lower() in "aeiou":
            count += 1

    return count

assert count_vowels("Armand") == 2
assert count_vowels("hello") == 2
assert count_vowels("aeiou") == 5
assert count_vowels("gym") == 0
assert count_vowels("Entourage") == 4

# Problem 6
def fizzbuzz(n):
    result = []

    for n in range(1, n + 1):
        if n % 15 == 0:
            result.append("fizzBuzz")
        elif n % 3 == 0:
            result.append("fizz")
        elif n % 5 == 0:
            result.append("buzz")
        else:
            result.append(n)

    return result

print(fizzbuzz(15))

assert fizzbuzz(33) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzBuzz"]
assert fizzbuzz(1) == [1]
assert fizzbuzz(5) == [1, 2, "fizz", 4, "buzz"]
assert fizzbuzz(15)[-1] == "fizzBuzz"
