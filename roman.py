"""Convert to and from Roman numerals"""

# Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

# Define digit mapping
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC',  90),
                   ('L',   50),
                   ('XL',  40),
                   ('X',   10),
                   ('IX',   9),
                   ('V',    5),
                   ('IV',   4),
                   ('I',    1))

def toRoman(n):
    """Convert integer to Roman numeral

    The romanNumeralMap is arranged in tuples of (numeral, integer)
    To convert an integer to Roman numeral representation, iterate
    through the romanNumeralMap subtracting the largest integer value 
    that is less than or equal to the input n and adding the numeral value
    to result.
    Lather rinse repeat."""

    if not (0 < n < 4000):
        raise OutOfRangeError, "number out of range (must be 1..3999)"
    if int(n) <> n:
        raise NotIntegerError, "non-integers can not be converted"

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def fromRoman(s):
    """Convert Roman numeral to integer"""
    result = 0
    index = 0


