from GameCharacter import GameCharacter


# Subclass for Warrior
class Warrior(GameCharacter):
    # Constructor function that is called when the create a new Warrior character
    # Warrior gets initiated with 10 pts of attack power, and 5 pts of defense
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        ...
        # TODO: fill me

    # Function that is called when the character is attacks a normal attack
    # Return the amount of damage dealt
    # Warrior attacks with attack_power * 1
    def attack(self) -> int:
        ...
        # TODO: fill me

    # Function that is called when the character defends from an incoming attack.
    # health is reduce from the damage - defense
    # Return the amount of health remaining
    def defend(self, damage: int) -> int:
        ...
        # TODO: fill me

    # Function that is called when we use our special ability
    # Warrior special ability is called Shield Block, and does (defense * 2) of damage
    # returns a tuple containing the name of the ability and the damage dealt
    def special_ability(self) -> (str, int):
        ...
        # TODO: fill me

    # Function that is called when we increase a level.
    # Warrior gains 2 pt of attack_power; 1 pt of defense; and 5 pt of max_health
    def improve_stats(self):
        ...
        # TODO: fill me
