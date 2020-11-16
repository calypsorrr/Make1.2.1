#!/usr/bin/env python


"""Calculator.py: How a calculator works."""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def main():

    x = input("Give me a number ")                                        # asking a number from the user
    y = input("give me another number ")                                  # asking another number from the user


    print("The sum of the 2 numbers you gave me is "+str(int(x)+int(y)))  # printing de sum of the numbers the user gave me

if __name__ == '__main__':  # code to execute if called from command-line
    main()