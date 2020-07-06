# Instructions:
# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

# [4, 3, 2, 5] would return [4, 3, 2, 6]


# My Solution
def up_array(arr):
    if not arr:
        return None
    result = []
    for num in arr:
        if num < 0 or num > 9:
            return
        else:
            result.append(str(num))
    result = int("".join(result)) + 1
    return [int(num) for num in str(result)]


# Sample Tests
Test.assert_equals(up_array([2, 3, 9]), [2, 4, 0])
Test.assert_equals(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
Test.assert_equals(up_array([1, -9]), None)


# Top Answer
def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
