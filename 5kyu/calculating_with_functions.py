# Instructions:
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# My Solution
def zero(operation="* 1"):
    return int(eval(f"0 {operation}"))


def one(operation="* 1"):
    return int(eval(f"1 {operation}"))


def two(operation="* 1"):
    return int(eval(f"2 {operation}"))


def three(operation="* 1"):
    return int(eval(f"3 {operation}"))


def four(operation="* 1"):
    return int(eval(f"4 {operation}"))


def five(operation="* 1"):
    return int(eval(f"5 {operation}"))


def six(operation="* 1"):
    return int(eval(f"6 {operation}"))


def seven(operation="* 1"):
    return int(eval(f"7 {operation}"))


def eight(operation="* 1"):
    return int(eval(f"8 {operation}"))


def nine(operation="* 1"):
    return int(eval(f"9 {operation}"))


def plus(num):
    return f"+ {num}"


def minus(num):
    return f"- {num}"


def times(num):
    return f"* {num}"


def divided_by(num):
    return f"/ {num}"


# Sample Tests
Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)


# Top Answer
def zero(f=None): return 0 if not f else f(0)
def one(f=None): return 1 if not f else f(1)
def two(f=None): return 2 if not f else f(2)
def three(f=None): return 3 if not f else f(3)
def four(f=None): return 4 if not f else f(4)
def five(f=None): return 5 if not f else f(5)
def six(f=None): return 6 if not f else f(6)
def seven(f=None): return 7 if not f else f(7)
def eight(f=None): return 8 if not f else f(8)
def nine(f=None): return 9 if not f else f(9)


def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x/y
