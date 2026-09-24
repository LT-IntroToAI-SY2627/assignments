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
assert get_first([1, 2, 3]) == 1

# Problem 2
def list_min(lst):
    return min(lst) if lst else None
assert list_min([3, 1, 4, 1, 5]) == 1

# Problem 3
def sum_positive(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total
assert sum_positive([1, -2, 3, -4, 5]) == 9
    

# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

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
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
