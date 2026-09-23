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
    if lst:
        return lst[0]
    else:
        return None


# Problem 2
def list_min(lst):
    if lst:
        minimum = lst[0]
        for item in lst:
            if item < minimum:
                minimum = item
        return minimum
    else:
        return None


# Problem 3
def sum_positive(lst):
    if lst:
        total = 0
        for item in lst:
            if item > 0:
                total += item
        return total
    else:
        return 0


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    if lst:
        unique_lst = [lst[0]]
        for item in lst[1:]:
            if item != unique_lst[-1]:
                unique_lst.append(item)
        return unique_lst
    else:
        return []

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    if lst:
        return lst[::2]
    else:
        return []

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    if lst:
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                return False
        return True
    else:
        return True

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
