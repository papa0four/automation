#!/usr/bin/env python3
def is_phone_number(text: str) -> bool:
    if (len(text) < 10 or len(text) > 14):
        return False

    if len(text) == 10:
        for i in range(0, len(text)):
            if not text[i].isdecimal():
                return False
        return True
    
    elif len(text) == 12:
        if (text[3] == '-' and
            text[7] == '-'):
            for i in range(0, 3):
                if not text[i].isdecimal():
                    return False
            for i in range(4, 7):
                if not text[i].isdecimal():
                    return False
            for i in range(8, 12):
                if not text[i].isdecimal():
                    return False
            return True

        else:
            return False
    
    elif len(text) == 14:
        if (text[0] == '(' and
            text[4] == ')' and
            text[5] == ' ' or
            text[5] == '-' and
            text[9] == ' ' or
            text[9] == '-'):
            for i in range(1, 4):
                if not text[i].isdecimal():
                    return False
            for i in range(6, 9):
                if not text[i].isdecimal():
                    return False
            for i in range(10,14):
                if not text[i].isdecimal():
                    return False
            return True            
    else:
        return False

if __name__ == '__main__':
    print('Testing is_phone_number function:\n')

    print('Testing False len < 10')
    if is_phone_number('1234567') is False:
        print('success')
    else:
        print('failed on too short test')

    print('Testing False len > 14')
    if is_phone_number('123456789012345') is False:
        print('success')
    else:
        print('failed on too long test')

    print('Testing True 10 digit: 1234567890')
    if is_phone_number('1234567890'):
        print('success')
    else:
        print('failed on 10 digit test')

    print('Testing True 12 digit: 123-456-7890')
    if is_phone_number('123-456-7890'):
        print('success')
    else:
        print('failed on 12 digit test')

    print('Testing True on 14 digit spaces: (123) 456 7890')
    if is_phone_number('(123) 456 7890'):
        print('success')
    else:
        print('failed on 14 digit spaces test')

    print('Testing True on 14 digit tac: (123)-456-7890')
    if is_phone_number('(123)-456-7890'):
        print('success')
    else:
        print('failed on 14 digit test tac')

    print('Testing False 10 digit: 123apple45')
    if is_phone_number('123apple45') is False:
        print('success')
    else:
        print('failed on 10 digit False test')

    print('Testing False 12 digit: 123456789012')
    if is_phone_number('123456789012') is False:
        print('success')
    else:
        print('failed on 12 digit False')

    print('Testing False 14 digit: (sam) 123 4567')
    if is_phone_number('(sam) 123 4567') is False:
        print('success')
    else:
        print('failed on 14 digit false')

