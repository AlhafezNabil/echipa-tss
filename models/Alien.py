from Character import Character


class Alien(Character):
    def __init__(self, name, strength, advancedTech):
        super().__init__(name, strength)
        self.advancedTech = advancedTech

    def __str__(self):
        return f"{self.name} {self.strength} {self.advancedTech}"

    def __gt__(self, other):
        if isinstance(other, Alien) and self.advancedTech and not other.advancedTech:
            return True
        elif isinstance(other, Alien) and self.advancedTech == other.advancedTech:
            return self.strength > other.strength
        return self.strength > other.strength
