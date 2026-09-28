# gh5.py
# GH-5: String Manipulation
# Introduction to AI | Lane Tech College Prep
# Name: [Jhonxel De Jesus]

# =============================================================================
# IN-CLASS PROBLEMS
# Work through these together in class.
# =============================================================================

# Problem 1
def make_greeting(name: str) -> str:
    return f"Hello {name}, welcome to the Lane Tech Info Bot!"
print(make_greeting("Jhonxel"))


# Problem 2
def clean_input(text: str) -> str:
    return text.strip().lower()
print(clean_input("   Hello World!   How many pizzas can you eat?   "))


# =============================================================================
# INDEPENDENT PROBLEMS
# Complete these on your own.
# Read the README for descriptions.
# =============================================================================

# Problem 3
def count_words(text):
    if text == "":
        return 0
    else:
        return len(text.split())

assert count_words("hello world") == 2
print(count_words("hello world"))
assert count_words("Lane Tech College Prep") == 4
print(count_words("Lane Tech College Prep"))
assert count_words("") == 0


# Problem 4
def initials(full_name):
    pass

assert initials("Alex Johnson") == "A.J."
assert initials("Mr. Berg") == "M.B."
assert initials("Lane Tech College Prep") == "L.T.C.P."
