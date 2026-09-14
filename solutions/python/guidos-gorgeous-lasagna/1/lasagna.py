"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20
elapsed_bake_time = 30

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    Parameters:
        number_of_layers (int): The total layers being preparaed.

    Returns:
        int: The total preparation time (in minutes) derived from 'number_of_layers * x'.

    Function that takes the actual number of layers being prepared for the lasagna, and deriving the time to prepare based on x.
    """
    return number_of_layers * 2

preparation_time_in_minutes(2)

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time elapsed in minutes.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
        number_of_layers (int): The total layers being preparaed.

    Returns:
        int: The elapsed bake time (in minutes) derived from 'elapsed_bake_time' and 'number_of_layers'.

    Function that takes total elapsed time and adds in preparation time.
    """
    return (number_of_layers * 2) + elapsed_bake_time

elapsed_time_in_minutes(3,20)

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
