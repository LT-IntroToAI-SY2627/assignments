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
    return lst[0]
assert get_first([1, 2, 3]) == 1
assert get_first(['a', 'b', 'c']) == 'a'


# Problem 2
def list_min(lst):
    x = lst[0]
    for i in range(len(lst)):
        if lst[i] < x:
            x = lst[i]
    return x
assert list_min([3, 1, 4, 1, 5]) == 1
assert list_min([-1, -5, 0]) == -5


# Problem 3
def sum_positive(lst):
    x = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            x += lst[i]
    return x
assert sum_positive([1, -2, 3, -4, 5]) == 9
assert sum_positive([-1, -2, -3]) == 0


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    new_list =[]
    for i in range(len(lst)):
        if i % 2 == 0:
            new_list.append(lst[i])
    return new_list

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    pass

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
