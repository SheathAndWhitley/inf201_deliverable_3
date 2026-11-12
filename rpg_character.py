
from rpg_items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon): Optional weapon for the character (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.weapon = weapon
        self.damage = damage

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon:
            target.take_damage(self.weapon.roll_damage())  # Use the weapon's damage roll
        else:
            target.take_damage(self.damage)  # Use the take_damage method of the target

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    def take_damage(self, damage: int) -> None:
        """Method to handle taking damage, affects only own HP"""
        self._hp -= damage
        self._hp = max(self._hp, 0)  # HP cannot go below 0


    def heal(self, amount: int) -> None:
        """Method to heal the character, cannot exceed max HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot exceed max HP

    @property
    def is_alive(self) -> bool:
        """Property to check if the character is alive (HP > 0)"""
        return self._hp > 0


class Warrior(Character):
    """
    Warrior, subclass of Character 
    Has a new attribute armor: int with default value 5
    Armor reduces incoming damage by its value, but cannot reduce damage below 0
    """

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Initialise the Warrior

        Args:
            name (str): The name of the warrior.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon): Optional weapon for the character (default = None)
            armor (int): Armor value that reduces incoming damage (default = 5)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        """Override take_damage to account for armor"""
        effective_damage = max(damage - self.armor, 0)  # Armor reduces damage but not below 0, armour doesn't heal the warrior.
        super().take_damage(effective_damage)  # Call the parent method to apply damage


class Mage(Character):
    """
    Mage, subclass of Character 
    Has new attributes mana: int and mana_max: int, both defaulting to 30
    Can attack using mana, when available, instead of regular damage
    """

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Initialise the Mage

        Args:
            name (str): The name of the mage.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon): Optional weapon for the character (default = None)
            mana (int): Mana value that allows special attacks (default = 30)
            mana_max (int): Max mana value (default = 30)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = mana

    def attack(self, target) -> None:
        """Override attack to use mana if available"""
        if self.mana >= 10:
            # Use 10 mana to perform double damage attack, uses basic damage not weapon
            target.take_damage(self.damage * 2)
            self.mana -= 10  # Reduce mana by 10
        else:
            # If not enough mana, perform regular attack, using weapon if available
            super().attack(target)
            self.mana += 5 # Regenerate 5 mana when not using special attack, but not exceeding mana_max
            self.mana = min(self.mana, self.mana_max)  # Ensure mana does not exceed mana_max
