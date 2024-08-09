#!/usr/bin/python3
"""
Write a method that calculates the fewewst number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """Create a function that returns an integer, if n is impossible to achieve, return 0"""

    current = 1
    begin = 0
    count = 0
    while current < n:
        check = n - current
        if (check % current == 0):
            begin = current
            current += begin
            count += 2
        else:
            current += begin
            count += 1
    return count
