"""
Write a function that takes a string as an argument and returns the number of capital letters in the string

Hint: 'foo'.upper() returns 'FOO'
"""


def f(string):
    count = 0
    for letter in string:
        if letter.isalpha() and letter == letter.upper():
            count += 1
    return count
print(f('The Rain in Spain'))