#!/usr/bin/env python


import time


"""Stopwatch.py: How a stopwatch works."""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def main():

    SECOND = 0
    MINUTE = 0
    HOUR = 0

    while True:
        if SECOND == 60:
            SECOND = 0
            MINUTE = 1
        if MINUTE == 60:
            MINUTE = 0
            HOUR = 1
        print(HOUR, MINUTE, SECOND)
        time.sleep(1)
        SECOND += 1

if __name__ == '__main__':  # code to execute if called from command-line
    main()