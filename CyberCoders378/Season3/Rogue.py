import random

from GameCharacter import GameCharacter


# Subclass for Rogue
class Rogue(GameCharacter):
    # Constructor function that is called when the create a new Rogue character
    # Rogue gets initiated with 7 pts of attack power, and 10 pts of evasion
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        ...
        # TODO: fill me

    # Function that is called when the character is attacks a normal attack
    # Return the amount of damage dealt
    # Rogue attacks with attack_power * 1
    def attack(self) -> int:
        ...
        # TODO: fill me

    # Function that is called when the character defends from an incoming attack.
    # Rogue use evasion to completely evade the attack at evasion% (e.g. if evade == 10 that is 10% chances to evade)
    # Return the amount of health remaining
    def defend(self, damage: int) -> int:
        ...
        # TODO: fill me

    # Function that is called when we use our special ability
    # returns a tuple containing the name of the ability and the damage dealt
    # Rogue special ability is called Backstab, and does (attack_power * 2) 30% of the time of damage
    def special_ability(self) -> (str, int):
        ...
        # TODO: fill me

    # Function that is called when we increase a level.
    # Warrior gains 1.5 pt of attack_power; 1 pt of evasion; and 3 pt of max_health
    def improve_stats(self):
        ...
        # TODO: fill me
