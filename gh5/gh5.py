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
    return "Hello " + name + "!"


# Problem 2
def clean_input(text):
    return text.strip().lower() # Strip function removes trailing/leadingwhitespace, lower converts to lowercase 


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    return len(text.split()) # Split function returns list of substrings separated by a deliminator (default space)

assert count_words("hello world") == 2
assert count_words("Lane Tech College Prep") == 4
assert count_words("") == 0


# Problem 4
def initials(full_name):
    output = ""
    names = full_name.split()
    for name in names:
        output += name[0].upper() + "."
    return output

assert initials("Alex Johnson") == "A.J."
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
