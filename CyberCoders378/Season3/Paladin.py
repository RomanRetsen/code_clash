from GameCharacter import GameCharacter


class Paladin(GameCharacter):
    # Constructor function that is called when the create a new Paladin character
    # Paladin gets initiated with 9pts of attack power, and 6pts of defense
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        ...
        # TODO: fill me

    # Function that is called when the character is attacks a normal attack
    # Return the amount of damage dealt
    # Paladin attacks with attack_power * 1
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
    # Paladin special ability is called Heal, and does (level * 5) damage and heal by the same amount
    def special_ability(self) -> (str, int):
        ...
        # TODO: fill me

    # Function that is called when we increase a level.
    # Paladin gains 1.5 pt of attack_power; 1 pt of defense; and 5 pt of max_health
    def improve_stats(self):
        ...
        # TODO: fill me

