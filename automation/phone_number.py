#!/usr/bin/env python3

import argparse
import re
from argparse import RawTextHelpFormatter

def get_arg() -> str:
    parser = argparse.ArgumentParser(description='Phone Number Validator',
                                    formatter_class=RawTextHelpFormatter)
    parser.add_argument('phone_number', type=str, action='store', nargs='+',
                        help='takes a 10, 12, 13, or 14 digit American phone number as a string:\n' \
                             'examples:\n<requires no quotes> - 1234567890, 123-456-7890\n' \
                             '<requires quotes> - "123 456 7890", "(123)456-7890, ' \
                             '"(123)456 7890",\n\t\t    "(123) 456 7890", "(123)-456-7890"')
    pnum = parser.parse_args()
    return pnum.phone_number[0]

def is_phone_number(text: str) -> bool:
    if (len(text) < 10 or len(text) > 14):
        return False


    """
    REGEX EXPLAINED:
        1st pairing of \d{3}[-\.\s]?? - handles first group of 3 digits followed by
        '-', '.', or ' '

        2nd pairing of \d{3}[-\.\s]?? - handles second group of 3 digits followed by
        '-', '.', or ' '

        1st pairing of \d{4} - handles last group of 4 digits

        | - bitwise or operator for alternative pairings 

        \(\d{3}\) - handles 3 digit area codes enclosed in ()

        \s* - handles all ' ' characters (special character)

        3rd pairing of \d{3}[-\.\s]?? - handles group of three digits that follow ' '
        and then is followed by '-', '.', or ' '

        2nd pairing of \d{4} - handles last group of 4 digits

        | - bitwise or operator for alternative pairings

        4th pairing of \d{3}[-\.\s]?? - handles second group of 3 digits that follow ' '
        and then is followed by '-', '.', or ' '

        3rd pairing of \d{4} - handles last group of 4 digits that follow '-', '.', or ' '
    """
    regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|" \
            "\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|" \
            "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4})" 

    match = re.search(regex, text)
    if match is None:
        print(f"match.group(): {match.group}\ttype: {type(match.group())}")
        return False
    return True

if __name__ == '__main__':
    pnum = get_arg()
    if is_phone_number(pnum):
        print(f'{pnum} is valid')
        exit(0)      
    
    print('Number passed is not a valid phone number format')
    print('type ./phone_number.py -h for examples')
    exit(-1)

