# Instructions:

# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'

# My Solution
def solution(string):
    new_string = list(string)
    new_string.reverse()
    return "".join(new_string)


# Sample Tests
# Test.assert_equals(solution('world'), 'dlrow')
# Test.assert_equals(solution('hello'), 'olleh')
# Test.assert_equals(solution(''), '')
# Test.assert_equals(solution('h'), 'h')

# Top Answer

def solution(str):
    return str[::-1]
