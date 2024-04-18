from Character import Character


class Human(Character):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength)
        self.planet = planet

    def __str__(self):
        return f"{self.name} from {self.planet} with strength {self.strength}"

    def fight(self, other):
        if isinstance(other, Human):
            print("Humans cannot fight amongs eachother.")
        else:
            super().fight(other)
