# Instructions:
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.


# My Solution
def is_pangram(s):
    letters = []
    for char in s:
        if char.lower() not in letters and char.isalpha():
            letters.append(char.lower())
    return True if len(letters) is 26 else False


# Sample Tests
pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)


# Top Answer
# import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
