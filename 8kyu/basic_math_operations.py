# Instructions:

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples
# basic_op('+', 4, 7)         # Output: 11
# basic_op('-', 15, 18)       # Output: -3
# basic_op('*', 5, 5)         # Output: 25
# basic_op('/', 49, 7)        # Output: 7

# My Solution
def basic_op(operator, value1, value2):
    operations = {
        "+": value1 + value2,
        "-": value1 - value2,
        "*": value1 * value2,
        "/": value1 / value2
    }
    return operations[operator]


# Sample Tests
Test.describe("Basic tests")
Test.assert_equals(basic_op('+', 4, 7), 11)
Test.assert_equals(basic_op('-', 15, 18), -3)
Test.assert_equals(basic_op('*', 5, 5), 25)
Test.assert_equals(basic_op('/', 49, 7), 7)


# Top Answer
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
