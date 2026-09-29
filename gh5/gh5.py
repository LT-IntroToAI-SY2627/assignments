# gh5.py
# GH-5: String Manipulation
# Introduction to AI | Lane Tech College Prep
# Name:Alison Severin

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def make_greeting(name):
    return f"Hey {name}, welcome to the Lane Tech Info Bot!"

print(make_greeting("Alison"))

# Problem 2
def clean_input(text):
    return text.strip().lower()

print(" \n Hello world!  ")
print(clean_input("  Hello World!  ")) 


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    return len(text.split())

assert count_words("hello world") == 2
assert count_words("Lane Tech College Prep") == 4
assert count_words("") == 0


# Problem 4
def initials(full_name):
    parts = full_name.split()
    return ".".join(part[0].upper() for part in parts) + "."

assert initials("Alex Johnson") == "A.J."
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
