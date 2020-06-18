# Instructions:
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

# My Solution
def high(x):
    letters = list(" abcdefghijklmnopqrstuvwxyz")
    highest_word = ""
    high_score = 0
    for word in x.split(" "):
        current_score = 0
        for letter in word:
            current_score += letters.index(letter)
        if current_score > high_score:
            high_score = current_score
            highest_word = word
    return highest_word


# Sample Tests
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')


# Top Answer
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
