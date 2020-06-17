# Instructions:
# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest([2,2,1,2,1]) = [2,2,2,1]

# My Solution
from numpy.random import randint


def remove_smallest(numbers):
    result = numbers.copy()
    if result:
        result.pop(numbers.index(sorted(numbers)[0]))
    return result


# Sample Tests
Test.describe("remove_smallest")

Test.it("works for the examples")
Test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [
                   2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
Test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [
                   5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
Test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [
                   2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
Test.assert_equals(remove_smallest([]), [], "Wrong result for []")


def randlist():
    return list(randint(400, size=randint(1, 10)))


Test.it("returns [] if list has only one element")
for i in range(10):
    x = randint(1, 400)
    Test.assert_equals(remove_smallest(
        [x]), [], "Wrong result for [{}]".format(x))

Test.it("returns a list that misses only one element")
for i in range(10):
    arr = randlist()
    Test.assert_equals(len(remove_smallest(arr[:])), len(
        arr) - 1, "Wrong sized result for {}".format(arr))


# Top Answer
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
