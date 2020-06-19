# Instructions:
# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

# My Solution
from collections import Counter


def count(string):
    return {letter: string.count(letter) for letter in string}


# Sample Tests
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})


# Top Answer
def count(string):
    return Counter(string)
