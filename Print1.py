#!/usr/bin/env python


"""
Print.py: How a Character works.
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():

    WORD = input("Give me a word user ")                                    # asking the user for a word

    print("This is how many characters are in your word "+str(len(WORD)))   # printing out the characters of that word


if __name__ == '__main__':  # code to execute if called from command-line
    main()