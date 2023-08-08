#!/usr/bin/python3
for digitOne in range(0, 8):
    for digitTwo in range((digitOne + 1), 10):
        print("{:d}{:d}".format(digitOne, digitTwo), end=", ")
print("89")
