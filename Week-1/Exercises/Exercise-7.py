"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint

def check_int(s):
    """ Check if string 's' represents an integer. """
    s = str(s)

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

#So far, everything keeps the same as in human-guess-a-number.py
# Starting from this session, I need user to give responses to my guess rather than the user's guess of an integer.

def input_response(prompt):
    """ Asks user for a response. The uses's response should use the valid responses I set nelow. """
    response = input(prompt).lower() # Ask the user for their responses, turn input into lowercase
    while response not in ['l','h','c']: # Repeat until the user inputs a valid response
        print("Invalid response. Please, enter 'l', 'h', or 'c'.")
        response = input(prompt).lower() 
    return response


# User select a number
print("Think of a number between 1 and 100, and I will try to guess it!")

low=1
high=100
guess = int((low + high) / 2) # The first guess will be the median

while True:
    print("My guess is:", guess)
    response = input_response("Is my guess correct, too low or too high?\nPlease reply c if it's correct, l if it's low, and h if it's high.")
    if response == "l": # if the guess is too low, I will increase the low 
        low = guess + 1
    elif response == "h": # if the guess is too high, I will decrease the high
        high = guess - 1
    elif response == "c":
        print("The number you were thinking of is:", guess)
        break # if I had a correct guess, then end the game
    else:
        print("Please use valid input, response with 'l', 'h', or 'c'.")
    guess = int((low + high) / 2)  # use the updated low or high to have a new guess!