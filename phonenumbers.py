#__*__coding:utf-8__*__
import re

"""This parses phone numbers

The number is entered in a single field but the area code, trunk, number
and optionally an extension stored separately in a database.
Should accept the following numbers:
    • 800−555−1212
    • 800 555 1212
    • 800.555.1212
    • (800) 555−1212
    • 1−800−555−1212
    • 800−555−1212−1234
    • 800−555−1212x1234
    • 800−555−1212 ext. 1234
    • work 1−(800) 555.1212 #1234
\d means any numeric digit
\d{3} means match exactly three numeric digits
(\d{3}) makes it a group
groups() returns a tuple of the groups defined in the regex
\D any character except a numeric character

A summary of regex techniques used:
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

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$') 
# cannot handle extensions

phonePattern.search('800-555-1212').groups()
# print phonePattern.search('800-555-1212-1234').groups()


phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
# assumes numbers are separated by hyphens
# cannot work for spaces, commas or dots
# cannot work for numbers without an extension

phonePattern.search('800-555-1212-1234').groups()
phonePattern.search('800-555-1212')



phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
# + means 1 or more \D+ assumes a separator and cannot work without
# cannot work without an extension

phonePattern.search('800-555-1212-1234').groups()
phonePattern.search('800 555 1212 1234').groups()
#print phonePattern.search('80055512121234').groups()
#print phonePattern.search('800-555-1212').groups()



phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# cannot handle leading characters e.g. (800)

phonePattern.search('80055512121234').groups()
phonePattern.search('800.555.1212 x1234').groups()
phonePattern.search('900-555-1221').groups()
#print phonePattern.search('(800)5551212 x1234')



phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# does not work if the leading character is a numeric character 
# e.g. 1-800-.*?

phonePattern.search('(800)5551212 ext. 1234').groups()
phonePattern.search('900-555-1212').groups()
#print phonePattern.search('work 1-(800) 555.1212 #1234')



phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# works for all current cases

print phonePattern.search('(800)5551212 ext. 1234').groups()
print phonePattern.search('800-333-1212').groups()
print phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print phonePattern.search('80033312121234').groups()
