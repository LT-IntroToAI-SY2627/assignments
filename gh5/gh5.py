# gh5.py
# GH-5: String Manipulation
# Introduction to AI | Lane Tech College Prep
# Name: [Your Name Here]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def make_greeting(name):
    return f"Hey {name}, welcome to the Lane Tech Info Bot"


# Problem 2
def clean_input(text):
    return text.strip().lower()


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    if not text:
        return 0
    return len(text.split())

assert count_words("hello world") == 2
assert count_words("Lane Tech College Prep") == 4
assert count_words("") == 0


# Problem 4
def initials(full_name):
    parts = full_name.split()
    initials_list = [part[0].upper() for part in parts]
    return '.'.join(initials_list) + '.'

assert initials("Alex Johnson") == "A.J."
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
