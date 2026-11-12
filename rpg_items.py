from rpg_dice import Dice

class Weapon:
    """
    A class representing different types of weapons in the game.
    """
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the weapon with a name and a damage dice
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """
        Roll the damage dice to determine the damage dealt by the weapon
        """
        return self.damage_dice.roll()


