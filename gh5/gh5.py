# gh5.py
# GH-5: String Manipulation
# Introduction to AI | Lane Tech College Prep
# Name: [Your Name Here]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def make_greeting(name: str) -> str:
    return f"Hello, {name}!"
print(make_greeting("Jhonxel"))


# Problem 2
def clean_input(text):
    pass


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    pass

assert count_words("hello world") == 2
assert count_words("Lane Tech College Prep") == 4
assert count_words("") == 0


# Problem 4
def initials(full_name):
    pass

assert initials("Alex Johnson") == "A.J."
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
