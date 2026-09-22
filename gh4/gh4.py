# gh4.py
# GH-4: Lists
# Introduction to AI | Lane Tech College Prep
# Name: [Your Name Here]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def get_first(lst):
    return lst[0] if lst else None


# Problem 2
def list_min(lst):
    smallest = lst[0]
    for x in lst:
        if x < smallest:
            smallest = x
    return smallest

# Problem 3
def sum_positive(lst):
    total = 0
    for x in lst:
        if x > 0:
            total += x
    return total


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    unique_list = []
    for x in lst:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    result = [lst[i] for i in range(0, len(lst), 2)]
    return result

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
