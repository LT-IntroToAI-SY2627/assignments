# gh4.py
# GH-4: Lists
# Introduction to AI | Lane Tech College Prep
# Name: [Jackson Knight]

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
        min_value = lst[0]
        for i in range(len(lst)):
            if lst[i] < min_value:
                min_value = lst[i]
        return min_value
    else:
        return None


# Problem 3
def sum_positive(lst):
    total = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            total += lst[i]
        else:
            total += 0
    return total


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    new_lst = []
    for item in lst:
            for new_item in new_lst:
                if item == new_item:
                    break
            else:
                new_lst.append(item)
    return new_lst

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    new_Lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            new_Lst.append(lst[i])
    return new_Lst

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
