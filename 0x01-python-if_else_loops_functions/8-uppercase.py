#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for letter in str:
        code = ord(letter)
        if (code >= ord('a') and code <= ord('z')):
            code -= 32
            letter = chr(code)
            upper += letter
        else:
            upper += letter
    print("{}".format(upper))
