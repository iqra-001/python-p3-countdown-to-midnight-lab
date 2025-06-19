  

import time

def countdown(number):
    """
    Counts down from the given integer to 1, printing the countdown message
    and "HAPPY NEW YEAR!" at the end.
    """
    while number >= 1:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    """
    Counts down from the given integer to 1, pausing for one second
    in each iteration and printing the countdown message.
    Prints "HAPPY NEW YEAR!" at the end.
    """
    while number >= 1:
        print(f"{number} SECOND(S)!")
        time.sleep(1)  # Pause for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")
