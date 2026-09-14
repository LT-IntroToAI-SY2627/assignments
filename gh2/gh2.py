# gh2.py
# GH-2: Functions & Conditionals
# Introduction to AI | Lane Tech College Prep
# Name: [Jackson Knight]

# Instructions:
# Replace each 'pass' with your solution.
# Do not change the function names or parameters.
# Add your own function at the bottom in the Your Contribution section.
# Run your file often to check for errors.

# =============================================================================
# PROBLEM 1: multiply(a, b)
# =============================================================================
# Write a function that takes two numbers and returns their product.
#
# multiply(3, 4)  ->  12
# multiply(5, 0)  ->  0
# multiply(2, 2)  ->  4

def multiply(a, b):
    return a * b

assert multiply(3, 4) == 12, "multiply test 1 failed"
assert multiply(5, 0) == 0,  "multiply test 2 failed"
assert multiply(2, 2) == 4,  "multiply test 3 failed"


# =============================================================================
# PROBLEM 2: classify_temp(temp)
# =============================================================================
# Write a function that takes a temperature in Fahrenheit and returns:
#   "hot"   if temp is 90 or above
#   "warm"  if temp is 70 to 89
#   "cool"  if temp is 50 to 69
#   "cold"  if temp is below 50
#
# classify_temp(95)  ->  "hot"
# classify_temp(75)  ->  "warm"
# classify_temp(55)  ->  "cool"
# classify_temp(30)  ->  "cold"

def classify_temp(temp):
    if temp >= 90:
        return "hot"
    elif temp >= 70 and temp < 90:
        return "warm"
    elif temp >= 50 and temp < 70:
        return "cool"
    elif temp < 50:
        return "cold"
    else:
        return "invalid temperature"

assert classify_temp(95) == "hot",  "classify_temp test 1 failed"
assert classify_temp(75) == "warm", "classify_temp test 2 failed"
assert classify_temp(55) == "cool", "classify_temp test 3 failed"
assert classify_temp(30) == "cold", "classify_temp test 4 failed"


# =============================================================================
# YOUR CONTRIBUTION
# =============================================================================
# Write your own original function below.
# Requirements:
#   - At least one parameter
#   - Uses a conditional (if/elif/else)
#   - Returns a value
#   - At least 2 asserts that test it

# Write your function here:

def isLaneTheBest(answer):
    if answer == "yes":
        return "Correct! Lane Tech is the best!"
    elif answer == "no":
        return "Incorrect! Lane Tech is the best!"
    else:
        return "Please answer with 'yes' or 'no'."

# Write your asserts here:
assert isLaneTheBest("yes") == "Correct! Lane Tech is the best!", "isLaneTheBest test 1 failed"
assert isLaneTheBest("no") == "Incorrect! Lane Tech is the best!", "isLaneTheBest test 2 failed"
assert isLaneTheBest("maybe") == "Please answer with 'yes' or 'no'.", "isLaneTheBest test 3 failed"