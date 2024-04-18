from Alien import Alien
from Astronaut import Astronaut
from Commander import Commander

alien1 = Alien("Zgyox",3.0,True)
astronaut1 = Astronaut("Francisca Pasare",4.5,"Pamant")
astronaut2 = Astronaut("Chiricuta Marina",1.2,"Pamant")
astronaut3 = Astronaut("Alhafez Nabil",-5.5,"Saturn")
commander1 = Commander("Merealbe Briana", 100, "Pamant")

print(alien1)
print(astronaut1)
print(astronaut2)
print(astronaut3)
print(commander1)

try:
    commander1.add_crew_member(astronaut1)
    commander1.add_crew_member(astronaut2)
    commander1.add_crew_member(astronaut3)
except ValueError as e:
    print(e)

print(commander1)

try:
    astronaut3.fight(astronaut2)
except ValueError as e:
    print(e)

try:
    commander1.fight(alien1)
except ValueError as e:
    print(e)

try:
    commander1.fight(astronaut1)
except ValueError as e:
    print(e)

print(alien1)
print(astronaut1)
print(astronaut2)
print(astronaut3)
print(commander1)
