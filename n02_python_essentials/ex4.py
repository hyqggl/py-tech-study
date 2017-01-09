# coding=utf-8
"""
Write a function that takes two sequences seq_a and seq_b as arguments and returns True if every element in seq_a is also an element of seq_b, else False

By “sequence” we mean a list, a tuple or a string
Do the exercise without using sets and set methods
"""


def f(seq_a, seq_b):
    is_subset = True
    for a in seq_a:
        if a not in seq_b:
            is_subset = False
    return is_subset


print(f([1, 2], [1, 2, 3]))
print(f([1, 2, 3], [1, 2]))


def f1(seq_a, seq_b):
    return set(seq_a).issubset(set(seq_b))
