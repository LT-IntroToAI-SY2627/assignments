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
    for number in numbers:
        total += number
    return total
# Problem 2
def count_above(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
        return count
    
    assert count_above([1, 2, 3, 4, 5], 3) == 2
    assert count_above([10, 20, 30], 25) == 1

# Problem 3
def categorize_scores(scores):
    categories = []
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

    assert categorize_scores([95, 82, 76, 61, 50]) == ["A", "B", "C", "D", "F"]
    assert categorize_scores([100, 85, 70, 55]) == ["A", "B", "C", "F"]
    print(categorize_scores([90, 80, 70, 60, 50]))  # Output: ['A', 'B', 'C', 'D', 'F']
    

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
