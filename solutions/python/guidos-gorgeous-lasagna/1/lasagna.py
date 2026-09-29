"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.

EXPECTED_BAKE_TIME = 40  # global constant
PREPARATION_TIME = 2 # global constant
def bake_time_remaining(elapsed_bake_time: int):
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

bake_time_remaining(25)

#TODO (student): Define the 'preparation_time_in_minutes()' function below.


def preparation_time_in_minutes(number_of_layers : int):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers(int): The number of layers

    Returns:
        int: The preparation time in minutes before baking
    
    Function that takes the number of layers as
    an argument and returns how many minutes the lasagna layers need to 
    based on the 'PREPARATION_TIME'.
    """
    return PREPARATION_TIME * number_of_layers

preparation_time_in_minutes(2)

# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time ):
    """Calculate the elapsed_time_in_minutes.

    Parameters:
        number_of_layers , elapsed_bake_time.

    Returns:
        int: The elapsed time in min derived from preparation_time_in_minutes & elapsed           bake time.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna elapsed
    based on the number_of_layers and elapsed_bake_time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

elapsed_time_in_minutes(2, 25 )

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
