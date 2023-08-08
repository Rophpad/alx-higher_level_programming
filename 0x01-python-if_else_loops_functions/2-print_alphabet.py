#!/usr/bin/python3
asciiValue = ord('a')
while (asciiValue <= ord('z')):
    letter = chr(asciiValue)
    print(letter, end='')
    asciiValue += 1
