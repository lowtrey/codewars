# Instructions:
# The goal of this exercise is to convert a string to a new string where each character in
# the new string is "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

# Notes
# Assertion messages may be unclear about what they display in some languages.
# If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

# My Solution
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(letter) == 1 else ")" for letter in word.lower()])


# Sample Tests
Test.assert_equals(duplicate_encode("din"), "(((")
Test.assert_equals(duplicate_encode("recede"), "()()()")
Test.assert_equals(duplicate_encode("Success"), ")())())",
                   "should ignore case")
Test.assert_equals(duplicate_encode("(( @"), "))((")


# Top Answer
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
