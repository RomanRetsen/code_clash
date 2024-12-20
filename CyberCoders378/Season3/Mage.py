from GameCharacter import GameCharacter


# Subclass for Mage
class Mage(GameCharacter):
    # Constructor function that is called when the create a new Mage character
    # Mage gets initiated with 15pts of attack power, and 2pts of defense
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        ...
        # TODO: fill me

    # Function that is called when the character is attacks a normal attack
    # Return the amount of damage dealt
    # Mage attacks with magic_power * 1
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
    # returns a tuple containing the name of the ability and the damage dealt
    # Mage special ability is called Fireball, and does (magic_power * 1.5) damage
    def special_ability(self) -> (str, int):
        ...
        # TODO: fill me

    # Function that is called when we increase a level.
    # Mage gains 3 pt of magic_power; 0.5 pt of defense; and 2 pt of max_health
    def improve_stats(self):
        ...
        # TODO: fill me