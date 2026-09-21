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
    get_first([10, 20, 30]) -> 10
    get_first9(["a", "b"]) -> "a"


# Problem 2
def list_min(lst):
    list_min([3,  1, 4, 1, 5]) -> 1
    list_min([10, 20, 5]) -> 5
    list_min([7]) -> 7



# Problem 3
def sum_positive(lst):
    sum_positive([1, -2, 3, -4, 5]) -> -9
    sum_positive([-1, -2, -3]) -> 0
    sum_positive([10, 20, 30]) -> 60

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
