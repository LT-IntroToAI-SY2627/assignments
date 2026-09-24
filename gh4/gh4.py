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

print(get_first([1, 2, 3]))  # Output: 1
print(get_first([]))         # Output: None

# Problem 2
def list_min(lst):
    if len(lst) == 0:
        return None
    min_val = lst[0]
    for num in lst:
        if x < min_val:
            min_val = x
    return min_val 
   
    print(list_min([3, 1, 4, 1, 5]))  # Output: 1
    print(list_min([]))               # Output: None




# Problem 3
def sum_positive(lst):
    total = 0
    for num in lst: 
        if num > 0:
            total += num
    return total

print(sum_positive([1, -2, 3, -4, 5]))  # Output: 9
print(sum_positive([-1, -2, -3]))        # Output: 0

# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 4
def remove_duplicates(lst): 
    

assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([1, 1, 2, 3, 4, 4, 4]) == [1, 2, 3, 4]


# Problem 5
def every_other(lst):
    

assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
assert every_other([10, 20, 30]) == [10, 30]
assert every_other([100, 200, 300, 400]) == [100, 300]


# Problem 6
def is_sorted(lst):
    pass

assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([2, 5,  7, 9]) == True 
