#!/usr/bin/python3
asciiValue = ord('a')
alphabet = ''
while (asciiValue <= ord('z')):
    letter = chr(asciiValue)
    if (letter == 'e' or letter == 'q'):
        pass
    else:
        alphabet += letter
    asciiValue += 1
print("{}".format(alphabet), end='')
