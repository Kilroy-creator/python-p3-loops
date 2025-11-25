#!/usr/bin/env python3

def happy_new_year():
    """Count down from 10 to 1, then print Happy New Year!"""
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """Return a list of squared integers using list comprehension"""
    return [num ** 2 for num in int_list]


def fizzbuzz():
    """Print numbers 1-100, with Fizz/Buzz/FizzBuzz for multiples"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)