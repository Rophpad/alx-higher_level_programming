#!/usr/bin/python3
def islower(c):
    code = ord(c)
    if (code >= ord('a') and code <= ord('z')):
        return True
    elif (code >= ord('A') and code <= ord('Z')):
        return False
