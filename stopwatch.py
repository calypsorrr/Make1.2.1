#!/usr/bin/env python


"""
Stopwatch.py: How a stopwatch works.
"""


import time


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():

    input("Press enter to start the timer ")                # User need to press start

    print("The timer has started")                          # Print out the timer had started

    start_timer = time.time()                               # The timer will start

    input("Press enter to stop the timer")                  # User can press enter to stop the timer

    end_time = time.time()                                 # Has the number of sec when the clock is stopped

    time_laps = end_time - start_timer                   # Has the value in seconds

    time_laps = float(time_laps)                        # This will let you see all the point values

    print("The time elapsed is", time_laps, "seconds")    # It will print out the seconds


if __name__ == '__main__':  # code to execute if called from command-line
    main()