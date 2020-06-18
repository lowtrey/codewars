# Instructions:
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples:

# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

# My Solution
def number(lines):
    result = []
    index = 1
    for line in lines:
        result.append(f"{index}: {line}")
        index += 1
    return result


# Sample Tests
test.assert_equals(number([]), [])
test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


# Top Answer
def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in xrange(len(lines))]
