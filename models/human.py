from models.character import Character


class Human(Character):
    def __init__(self, name, strength, planet):
        if not isinstance(planet, str):
            raise TypeError("Planet should be a string")
        super().__init__(name, strength)
        self._planet = planet

    @property
    def planet(self):
        return self._planet

    @planet.setter
    def planet(self, value):
        if not isinstance(value, str):
            raise ValueError("Planet must be a string.")
        self._planet = value

    def __str__(self):
        return f"{self.name} from {self.planet} with strength {self.strength}"

    def fight(self, other):
        if isinstance(other, Human):
            print("Humans cannot fight among each other.")
            raise ValueError("Crew members must be from the same planet.")
        else:
            super().fight(other)
