import re

"""Getting Roman Numerals

This is a module to confirm whether a sequence of letters adds up to
make a roman numeral.
"""

#NOTE: Roman numeral conventions:
# Fives cannot be repeated. That is V(5), L(50) and D(500)
# There can only be a maximum of three repetitions.
# To write a nine or a four you need to subtract the nearest ten
# 4=IV-> one less than five 9=IX-> one less than 10
# 90=XC-> 10 less than 100 99=XCIx-> 10 less than 100 and one less
# than 10
# Characters are additive except for fours and nines
# VIII=8, XX=20, XXV=25, LXX=70, LXXV=75, CCC=300, DCC=700

pattern = '''
          ^             # this is the start of the string
          M{0,3}        # This is the thousands. There can be no M
                        # or there can be between 1 and 3 M's

          (CM|CD|D?C{0,3}) # This is the hundreds CM=900, CD=400
                           # The ? means its optional
                           # | means only one of the 3 options can be
                           # found 
                           # Can be D(500) alone or D followed by between
                           # one and three C's(600-800)
                           # or zero to three C's without a D(0-300)

          (XC|XL|L?X{0,3}) # This is the hundreds
                           # There can be 90(XC) or 40(Xl) or any number from
                           # 10 to 30(one to three X's) or 50 to 80
                           # (L followed by zero to three X's)

          (IX|IV|V?I{0,3}) # This is the ones
                           # Can be 9(IX), 4(IV), 0-3(0 to 3 I's),
                           # or 5-8(V followed by 0 to 3 I's)

          $                # This is the end of the string
          '''

text = 'MMCMLXXVII'   #2977

print re.search(pattern, text, re.VERBOSE)

# re.VERBOSE => verbose output format ignoring whitespace and comments
