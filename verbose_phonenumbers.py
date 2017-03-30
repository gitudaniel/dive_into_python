# __*__coding:utf-8__*__
import re

"""Phone Numbers Verbose

This is the verbose implementation of parsing phone numbers with
comments detailing choice of characters used.
Groups are separated by a line of whitespace.

A summary of the regex techniques used:
• ^ matches the beginning of a string.
• $ matches the end of a string.
• \b matches a word boundary.
• \d matches any numeric digit.
• \D matches any non−numeric character.
• x? matches an optional x character (in other words, it matches an x zero or one times).
• x* matches x zero or more times.
• x+ matches x one or more times.
• x{n,m} matches an x character at least n times, but not more than m times.
• (a|b|c) matches either a or b or c.
• (x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object returned by re.search.
"""

phonePattern = re.compile(r'''
                # don't match beginning of string, number can
                # start anywhere

(\d{3})         # area code is first 3 digits e.g. '800'

\D*             # optional separator is any variety of non-digits
                # e.g. commas, spaces, hyphens, dots e.t.c.

(\d{3})         # trunk is 3 digits (e.g. '555')

\D*             # optional separator

(\d{4})         # rest of number is 4 digits

\D*             # optional separator

(\d*)           # extension is optional and can be any no of digits

$               # end of string
''', re.VERBOSE)

print phonePattern.search('work 1-(800) 555.1212 #1233').groups()
print phonePattern.search('800-555-1212').groups()
