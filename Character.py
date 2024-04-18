class Character:
    def __init__(self, name, strength):
        self.name = name
        if strength > 5:
            self.strength = min(strength, 5)
        else:
            self.strength = max(strength, 0)

    def __str__(self):
        return f"{self.name} {self.strength}"

    def __gt__(self, other):
        return self.strength > other.strength

    def fight(self, other):
        if self > other:
            self.strength = min(self.strength + 1, 5)
            print(f"{self.name} wins and now has strength {self.strength}")
        else:
            print(f"{other.name} wins and now has strength {other.strength}")
