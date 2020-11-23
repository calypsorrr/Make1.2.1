#!/usr/bin/env python


"""
Stopwatch.py: How a stopwatch works.
This is a program of my own to experment with. The real program is stopwatch.py
"""


import time


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():

    SECOND = 0                        # Second's are 0
    MINUTE = 0                        # Minute's are 0
    HOUR = 0                          # Hour's are 0

    while True:                       # This will asure that it wil do this
        if SECOND == 60:              # If the seconds are 60 then it will do this
            SECOND = 0                # Back to 0 seconds
            MINUTE = 1                # Minute goes to 1
        if MINUTE == 60:              # If minute's are 60 then it will do this
            MINUTE = 0                # Back to 0 minute's
            HOUR = 1                  # Hour's goes to 1
        print(HOUR, MINUTE, SECOND)   # Print Hour, Minute, Second
        time.sleep(1)                 # The programme will do nothing for 1 second
        SECOND += 1                   # Everytime at the end of the programme second's goes 1 up


if __name__ == '__main__':  # code to execute if called from command-line
    main()