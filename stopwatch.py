#!/usr/bin/env python


import time


"""Stopwatch.py: How a stopwatch works."""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

SECOND = 0
MINUTE = 0
HOUR = 0

input("Press enter to start the timer ")                # User need to press start

print("The timer has started")                          # Print out the timer had started

START_TIMER = time.time()                               # The timer will start

input("Press enter to stop the timer")                  # User can press enter to stop the timer

END_TIMER = time.time()                                 # Has the number of sec when the clock is stopped

TIME_LAPSED = END_TIMER - START_TIMER                   # Has the value in seconds

TIME_LAPSED = float(TIME_LAPSED)                        # This will let you see all the point values

print("The time elapsed is", TIME_LAPSED, "seconds")    # It will print out the seconds
