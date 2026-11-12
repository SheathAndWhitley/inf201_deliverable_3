from random import randint

class Dice:
    """
    A class to represent a dice with n >= 2 sides
    """
    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the dice with a given number of sides
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """
        Roll the dice and return a random number between 1 and the number of sides
        """
        return randint(1, self.sides)

    def __repr__(self) -> str:
        """
        Return a string representation of the dice
        """
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """
        Allow the dice to be called like a function to roll it
        """
        return self.roll()

