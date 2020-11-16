#!/usr/bin/env python


"""Age.py: How to calculate age."""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def main():

    YEAR = 2020                                                                   # this will be used for a calculation

    x = 50                                                                        # this will be used for a calculation

    AGE = input("How old are you user? ")                                          # asking the user for his age

    print("The year you where born in is "+str(int(YEAR)-int(AGE)))               # printing when he was born

    print("The year when you turn 50 is "+str(int(YEAR)-int(AGE)+int(x)))         # printing in what year you will become 50

if __name__ == '__main__':  # code to execute if called from command-line
    main()
