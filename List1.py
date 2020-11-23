#!/usr/bin/env python


"""
List.py: How a list works.
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():

    random_words = ["sum", "book", "bike", "lost"]               # a list of random words

    print(random_words)                                          # this wil print out random_words

    more_words = input("Give me some words user ").split()       # this wil ask the user for some words

    random_words.extend(more_words)                              # this wil extend the list of random_words

    print(random_words)                                          # this wil print out the new list with the new words


if __name__ == '__main__':  # code to execute if called from command-line
    main()
