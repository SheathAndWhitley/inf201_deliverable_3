from rpg_character import Character


class Battle:
    """
    A class representing a battle between two characters.
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the battle with a hero and an enemy.

        Args:
            hero (Character): The hero character.
            enemy (Character): The enemy character.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play a single round of the battle where both characters attack each other, if possible
        """

        if self.hero.is_alive and self.enemy.is_alive:
            print(f"{self.hero.name} attacks {self.enemy.name}!")
            self.hero.attack(self.enemy)
            print(f"{self.enemy.name} has {self.enemy.hp} HP left.")

        if self.enemy.is_alive:
            print(f"{self.enemy.name} attacks {self.hero.name}!")
            self.enemy.attack(self.hero)
            print(f"{self.hero.name} has {self.hero.hp} HP left.")

    def simulate_battle(self) -> None:
        """
        Simulate the battle until one character is defeated.
        """
        round_number = 1
        while self.hero.is_alive and self.enemy.is_alive:
            print(f"\n--- Round {round_number} ---")
            self.play_round()
            round_number += 1

        if self.hero.is_alive:
            print(f"\n{self.hero.name} wins the battle!")
        else:
            print(f"\n{self.enemy.name} wins the battle!")