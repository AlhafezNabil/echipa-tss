from models.human import Human


class Astronaut(Human):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength, planet)

    def __str__(self):
        return f"Astronaut {self.name} from {self.planet} with strength {self.strength}"
