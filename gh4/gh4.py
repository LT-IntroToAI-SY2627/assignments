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
    return min(lst) if lst else None


# Problem 3
def sum_positive(lst):
    return sum(x for x in lst if x > 0)


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    return lst[::2]

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    pass

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
