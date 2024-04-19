from models.character import Character


class Alien(Character):
    def __init__(self, name, strength, advancedTech):
        if not isinstance(advancedTech, bool):
            raise ValueError("Test that providing a non-boolean type for advancedTech raises an error")
        super().__init__(name, strength)
        self._advancedTech = advancedTech

    @property
    def advancedTech(self):
        return self._advancedTech

    @advancedTech.setter
    def advancedTech(self, value):
        if not isinstance(value, bool):
            raise ValueError("advancedTech must be a boolean value.")
        self._advancedTech = value

    def __str__(self):
        return f"{self.name} {self.strength} {'with' if self.advancedTech else 'without'} advanced technology"

    def __gt__(self, other):
        if isinstance(other, Alien) and self.advancedTech and not other.advancedTech:
            return True
        elif isinstance(other, Alien) and self.advancedTech == other.advancedTech:
            return self.strength > other.strength
        return self.strength > other.strength
