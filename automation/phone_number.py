#!/usr/bin/env python3

import argparse
import re
from argparse import RawTextHelpFormatter

def get_arg() -> str:
    parser = argparse.ArgumentParser(description='Phone Number Validator',
                                    formatter_class=RawTextHelpFormatter)
    parser.add_argument('phone_number', type=str, action='store', nargs='+',
                        help='takes a 10, 12, or 14 digit American phone number as a string:\n' \
                             'examples:\n<requires no quotes> - 1234567890, 123-456-7890\n' \
                             '<requires quotes> - "(123) 456 7890", "(123)-456-7890"')
    pnum = parser.parse_args()
    return pnum.phone_number[0]

def is_phone_number(text: str) -> bool:
    if (len(text) < 10 or len(text) > 14):
        return False

    regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??" \
            "\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??" \
            "\d{4}|\d{3}[-\.\s]??\d{4})"
    match = re.search(regex, text)
    if match is None:
        return False
    return True

if __name__ == '__main__':
    pnum = get_arg()
    if is_phone_number(pnum):
        print(f'{pnum} is valid')
        exit(0)      
    
    print('Number passed is not a valid phone number')
    print('type ./phone_number.py -h for examples')
    exit(-1)

