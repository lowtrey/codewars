# Instructions:
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase)
# and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


# My Solution
def duplicate_count(text):
    result = 0
    count = {}

    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for num in count.values():
        if num > 1:
            result += 1
    return result


# Sample Tests
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)


# Top Answer
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
