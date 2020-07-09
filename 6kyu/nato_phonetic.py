# Instructions:
# The idea for this Kata came from 9gag today.here

# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

# Like this:

# ** Input: ** If you can read

# ** Output: ** India Foxtrot Yankee Oscar Uniform Charlie Alfa November
# Romeo Echo Alfa Delta

# ** Some notes **

# Keep the punctuation, and remove the spaces.
# Use Xray without dash or space.


# My Solution
def to_nato(words):
    punctuation = '.,:;?!'
    dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', "H": "Hotel", 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike',
            'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}
    chars = [char.upper()
             for char in words if char.isalpha() or char in punctuation]
    result = [dict.get(val, val) for val in chars]
    return " ".join(result)


# Sample Tests
Test.describe("Basic Tests")
Test.assert_equals(to_nato('If you can read'), "India Foxtrot Yankee Oscar
                   Uniform Charlie Alfa November Romeo Echo Alfa Delta")
Test.assert_equals(to_nato('Did not see that coming'), "Delta India Delta
                   November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar
                   Mike India November Golf")


# Top Answer
def to_nato(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
