# Instructions:
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

# DNA_strand ("ATTGC") # return "TAACG"

# DNA_strand ("GTAT") # return "CATA"

# My Solution
import string


def DNA_strand(dna):
    result = []
    for letter in dna:
        if letter == "A":
            result.append("T")
        elif letter == "T":
            result.append("A")
        elif letter == "C":
            result.append("G")
        elif letter == "G":
            result.append("C")
    return "".join(result)


# Sample Tests
Test.assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")

# Top Answer
# I mistakenly imported maketrans from string instead of just string


def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG", "TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
