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

print (get_first([1, 2, 3]))  # Output: 1
print (get_first([]))         # Output: None

# Problem 2
def list_min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

print (list_min([3, 1, 4, 1, 5]))  # Output: 1
print (list_min([]))               # Output: None


# Problem 3
def sum_positive(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total

print (sum_positive([1, -2, 3, -4, 5]))  # Output: 9
print (sum_positive([-1, -2, -3]))      # Output: 0


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

print (remove_duplicates([1, 2, 2, 3, 3, 3]))  # Output: [1, 2, 3]
print (remove_duplicates([1, 1, 1]))            # Output: [1]
print (remove_duplicates([]))                   # Output: []

# Problem 5
def every_other(lst):
    return lst[::2]

print (every_other([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
print (every_other([10, 20, 30]))     # Output: [10, 30]
print (every_other([]))                # Output: []


# Problem 6
def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

print (is_sorted([1, 2, 3, 4, 5]))  # Output: True
print (is_sorted([1, 3, 2, 4, 5]))  # Output: False
print (is_sorted([]))               # Output: True
