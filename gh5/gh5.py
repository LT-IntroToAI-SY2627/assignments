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

    return f"Hello, {name}, welcome to the Lane Tech Info Bot!"
print(make_greeting("Alex"))


# Problem 2
def clean_input(text):
    return text.strip().lower()
print(clean_input("  Hello, World!  "))


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    return len(text.split())

print(count_words("hello world"))
print(count_words("Lane Tech College Prep"))
print(count_words(""))


# Problem 4
def initials(full_name):
    name_parts = full_name.split()
    return ".".join([part[0].upper() for part in name_parts]) + "."
print(initials("Alex Johnson"))
print(initials("Mr. Berg"))
print(initials("Lane Tech College Prep"))
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
