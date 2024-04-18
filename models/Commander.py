from Astronaut import Astronaut
from Human import Human


class Commander(Human):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength, planet)
        self.crew = []

    def add_crew_member(self, astronaut):
        if not isinstance(astronaut, Astronaut):
            raise ValueError("Only astronauts can be added to the crew.")
        if astronaut.planet != self.planet:
            raise ValueError("Crew members must be from the same planet.")
        self.crew.append(astronaut)

    def __str__(self):
        crew_names = ', '.join([astronaut.name for astronaut in self.crew])
        return f"Commander {self.name} from {self.planet} with strength {self.strength} and with crew [{crew_names}]"

