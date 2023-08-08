#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = -number
    lastDigit = number % 10
    print('{:d}'.format(lastDigit), end="")
    return lastDigit
