from models.astronaut import Astronaut
from models.human import Human


class Commander(Human):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength, planet)
        self._crew = []

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        for member in new_crew:
            if not isinstance(member, Astronaut) or member.planet != self.planet:
                raise ValueError("All crew members must be Astronauts from the same planet as the commander.")
        self._crew = new_crew

    def add_crew_member(self, astronaut):
        if not isinstance(astronaut, Astronaut):
            raise ValueError("Only astronauts can be added to the crew.")
        if astronaut.planet != self.planet:
            raise ValueError("Crew members must be from the same planet.")
        self._crew.append(astronaut)

    def __str__(self):
        crew_names = ', '.join([astronaut.name for astronaut in self._crew])
        return f"Commander {self.name} from {self.planet} with strength {self.strength} and with crew [{crew_names}]"
