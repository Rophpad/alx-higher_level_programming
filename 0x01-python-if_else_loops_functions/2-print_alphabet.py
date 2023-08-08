#!/usr/bin/python3
asciiValue = ord('a')
alphabet = ''
while (asciiValue <= ord('z')):
    letter = chr(asciiValue)
    alphabet += letter
    asciiValue += 1
print(f'{alphabet}', end='')
