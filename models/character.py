class Character:
    def __init__(self, name, strength):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        self._name = name
        self._strength = max(0, min(strength, 5))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Strength must be a number.")
        if value < 0 or value > 5:
            raise ValueError("Strength must be between 0 and 5.")
        self._strength = value

    def __str__(self):
        return f"{self._name} {self._strength}"

    def __gt__(self, other):
        return self._strength > other.strength

    def fight(self, other):
        if self > other:
            self.strength = min(self.strength + 1, 5)
            print(f"{self.name} wins and now has strength {self.strength}")
        else:
            print(f"{other.name} wins and now has strength {other.strength}")
