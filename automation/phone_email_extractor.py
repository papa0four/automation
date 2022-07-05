#!/usr/bin/env python3

# find phone numbers and email addresses on clipboard

import pyperclip
import re

'''
PNUM REGEX PURPOSE: line-by-line
area code
separator
first 3 digits
separator
last 4 digits
extension
'''

pnum = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# TODO: Create email regex
'''
EMAIL REGEX PURPOSE: line-by-line
username
@ symbol
domain name
dot-something
'''

email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

'''
use pyperclip and regex to find matches on clipboard
'''

text = str(pyperclip.paste())
matches = []
for groups in pnum.findall(text):
    num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        num += ' x' + groups[8]
    matches.append(num)
for groups in email.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard
'''
paste found results to clipboard
'''

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


