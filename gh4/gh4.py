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
print(list_min([3, 1, 4, 1, 5]))

# Problem 3
def sum_positive(lst):
    return sum(num for num in lst if num > 0)
print(sum_positive([-1, 2, -3, 4, 5]))


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 3, 3]))
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []


# Problem 5
def every_other(lst):
    return lst[::2]

print(every_other([1, 2, 3, 4, 5]))
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([]) == []


# Problem 6
def is_sorted(lst):
    pass

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([]) == True
