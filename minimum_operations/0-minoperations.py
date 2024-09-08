#!/usr/bin/python3
# def minOperations(n):
# characters = 1
# operations = 0
# copy = characters

# while characters < n:
# if (n - characters)%2 == 0:
# perform
# copy = characters
#           characters += copy
#          operations += 2
#      else:
# if operations == 0:
#                operations += 1
#  characters += copy
#  operations += 1
# return operations
# Minimum number of operations
"""
    perform minimum
    operations
  """


def minOperations(n):
    """
    get minimum double , and one
    operations
    """
    operations = 0
    characters = 2
    while n > 1:
        # ensure characters count is greater than 0
        # else return a zero
        while n % characters == 0:
            # while difference is even increase
            # operations by character count
            operations += characters
            # reduce the characters count by half
            n = n / characters
        # increase the characters
        characters += 1
    return operations
