# gh4.py
# GH-4: Lists
# Introduction to AI | Lane Tech College Prep
# Name: [Armand Peto]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def get_first(lst):
    if lst:
        return lst[0]
    return None
print(get_first([1, 2, 3]))  # Output: 1


# Problem 2
def list_min(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest
print(list_min([3, 1, 4, 1, 5]))  # Output: 1



# Problem 3
def sum_positive(lst):
    return sum(n for n in lst if n > 0)
result = sum_positive([1, -2, 3, -4, 5])
print(result)  # Output: 9 (1 + 3 + 5 = 9)

assert sum_positive([-2, -3, -39]) == 0

# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

#Example usage:
numbers = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([7, 8, 4, 5, 2, 1, 2, 4, 5, 6, 8, 4, 3, 3, 2, 9]) == [7, 8, 4, 5, 2, 1, 6, 3, 9]

# Problem 5
def every_other(lst):
    pass

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    pass

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
