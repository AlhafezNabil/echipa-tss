# echipa-tss



### [Articol original](https://onlinelibrary.wiley.com/doi/10.1002/cae.22642)

### [Cerintele](./tema_proiect_TSS.docx)

### [Materialele cursurlui](https://drive.google.com/drive/folders/1sE4SYCgyXNxyiW6oRFTWalut7mMOdIu2)

### [DEMO](https://youtu.be/g8Dw-8hYT6w)

## Features
- **First feature**: something.

## Technical Details
- **Language**: Python 3.9.x

## Running Tests
- Ensure functionality by running unit tests structured in the tests directory. Execute the following command in the root directory:   
`python -m unittest discover -s tests`


## Project Structure

```plaintext
echipa-tss/
│
├── models/
│   ├── __init__.py
│   ├── alien.py
│   ├── astronaut.py
│   ├── character.py
│   ├── commander.py
│   └── human.py
│
│
├── tests/
│   ├── __init__.py
│   └── unit/
│       ├── __init__.py
│       ├── constructor/
│       │   ├── __init__.py
│       │   ├── test_alien_constructor.py
│       │   ├── test_astronaut_constructor.py
│       │   ├── test_character_constructor.py
│       │   ├── test_commander_constructor.py
│       │   └── test_human_constructor.py
│       │
│       ├── fight_method/
│       │   ├── __init__.py
│       │   ├── test_character_fight_method.py
│       │   └── test_human_fight_method.py
│       │
│       ├── greater_operator/
│       │   ├── __init__.py
│       │   ├── test_alien_greater_operator.py
│       │   ├── test_character_greater_operator.py
│       │   └── test_human_greater_operator.py
│       │
│       ├── inheritance/
│       │   ├── __init__.py
│       │   ├── test_alien_inheritance.py
│       │   ├── test_astronaut_inheritance.py
│       │   ├── test_character_inheritance.py
│       │   ├── test_commander_inheritance.py
│       │   └── test_human_inheritance.py
│       │
│       ├── properties/
│       │   ├── __init__.py
│       │   ├── test_alien_properties.py
│       │   ├── test_astronaut_properties.py
│       │   ├── test_character_properties.py
│       │   ├── test_commander_properties.py
│       │   └── test_human_properties.py
│       │
│       └── str/
│           ├── __init__.py
│           ├── test_alien_str.py
│           ├── test_astronaut_str.py
│           ├── test_character_str.py
│           ├── test_commander_str.py
│           └── test_human_str.py
└──
```

## Evaluarea automată a principilor de OOP
## Testare unitară în Python

În cadrul acestei lucrări, ne concentrăm pe dezvoltarea unei metode de evaluare automată (AA) pentru un domeniu care prezintă unele provocări în evaluarea sa practică: programarea orientată pe obiecte (OOP). Pentru a evalua corectitudinea aplicării principiilor OOP într-o aplicație reală, ne folosim de testarea unitară. 
Accentul este pus pe încurajarea elevilor să înțeleagă și să aplice corect principiile OOP complexe, precum și pe capacitatea lor de a proiecta în mod adecvat clasele și relațiile dintre acestea. În acest sens, prezentăm un studiu de caz bazat pe o sarcină practică, în care elevii sunt solicitați să creeze personaje pentru un joc video. Această sarcină este remarcabilă prin faptul că este incrementală și abordează toate cele patru principii OOP într-un singur context.
Cele patru principii de OOP sunt: 
1.	Încapsularea constă în gruparea datelor și metodelor conexe într-o singură entitate (clasa). Încapsularea permite, de asemenea, ca codul să fie legat liber. Încapsularea permite modificarea datelor numai prin intermediul metodelor, ceea ce face codul mai robust. 
2.	Abstracția permite ascunderea membrilor, metodelor și implementării în interiorul clasei. Există trei cuvinte cheie asociate cu cât de ascunși sunt membrii clasei:

•	public - dacă membrul clasei este declarat public, atunci acesta poate fi accesat oriunde.
•	protected - dacă membrul clasei este declarat ca protected, atunci acesta poate fi accesat numai în cadrul clasei în sine și prin moștenirea claselor copil.
•	privat - dacă membrul clasei este declarat ca privat, atunci acesta poate fi accesat numai de clasa care definește membrul.
3.	Moștenirea este un principiu foarte util al OOP care construiește relații între clase. Acest lucru le permite să împărtășească membrii clasei și metodele. Moștenirea surprinde o relație „este-o” între clase. Vă permite să luați o clasă existentă și să o specializați și/sau să o extindeți
4.	Polimorfismul înseamnă că o metodă poate face față diferitelor tipuri de intrări. Apoi, același cod poate fi aplicat mai multor tipuri de date. Există două tipuri de polimorfism: supraîncărcare și suprascriere.
•	Supraîncărcarea permite unei clase să aibă mai multe metode cu același nume, dar un set diferit de parametri și implementare. De exemplu, unul foarte popular este operatorul + (de exemplu, pentru concatenarea a două șiruri).
•	Suprascrierea are loc atunci când se înlocuiește o metodă moștenită cu o altă metodă având aceeași semnătură. 
In continuare prezentăm un studiu de caz real al unei aplicații OOP — „implementarea personalor unui joc video, Supraviețuirea în Cosmos” — care aplică toate cele patru principii OOP pentru a rezolva acest singur scenariu.


Clasa Alien
Atribute:
•	name: nume alien (ex: “Zyglorx”)
•	strength: nivel de forta [0-5]
•	advancedTech: are tehnologie avansata [True/False]
Metode asociate:
1.	Contructor pentru initializare: 
		Ex: alien1 = Alient(“Zyglorx”, 3, true)
In Python, constructorul este o metodă specială numită __init__.
2.	Proprietățile de accesare și modificare a valorilor tuturor:
	Ex: alien1.name = “Xing”;
3.	Metoda __str__, care este o metodă specială din Python care este utilizată pentru afișarea informațiilor unui obiect într-o reprezentare șir frumos formatată.
	Ex: nume ani experinta viza de munca
		Zyglorx 3 True
4.	Supraîncărcarea operatorul > (__gt__) determină daca un extraterestu are mai multa putere in ceea ce priveste lupta decat un alt extraterestru. Extraterestrul ce detine o tehnologie avansata este mai puternic decat unul ce nu dispune de una. Daca amandoi dispun de tehnologie avansata , atunci o sa fie mai puternic extraterestrul cu forta mai mare.
5.	Extraterestrul are o metoda numita, “fight” care se realizeaza cu un alt extraterestru. Daca un extraterestru este mai puternic decat altul, atunci castiga si puterea lui creste cu 1. Extraterestrul castigator este afisat pe ecran
Scopul nostru este sa implementan atat teste pentru gestionarea erorilor de tipuri si valori pentru atributele clasei, dar si pentru verifcarea tuturor functionalitatilor clasei Alien.
In aplicatia nostra nu avem doar clasa Alien, exista si alte case precum, clasele “Astronaut” si “Commander” ce au atat atributele nume si forta  (cs si obiectele din clasa Alien), dar au si anumite atribute suplimentare:
•	planet: planeta de origine
•	crew: echipajul (comandantii au un atriput suplimentar ce este reprezentat de o lista de tip Astronaut).
Aceasta lista reprezinta astronoutii ce se afla sub comanda unui comandant. Nu exista o lista maxima de astronauti ce pot sa fie sub conducerea unui comandant, insa ei trebuie sa fie de pe aceeasi planeta. 
Astronautii si comandantii au aceleasi metode ca si Extragerestrii, insa exista si cateva diferente. 
•	Toate personajele se pot folosi de operatorul > cu orice alt tip de caracter, Nu trebuie sa uitam, insa, ca doar extraterestrii dispun de tehnologie avansata.
•	Comandantii si astronautii se pot confrunta doar cu extraterestrii. Daca se incearca o lupta intre acestia se va afisa un mesaj de eroare.
•	Mesajul _str_ returneaza reprezentarea in sir a instantelor in acest format. In cazul comandantilor, lista astronautilor se va afisa intre paranteze drepte.
Observam ca dispunem de trei clase Alien, Astronaut si Commander. Clasele Astrounaut si Commander au in comun planeta de provenienta si alte metode specializate(operatorul >). Pentru aceste doua clase putem sa formam o super clasa, aceaasta poate sa fie numita clasa Human.
Ceea ce am omis, este faptul ca toate clasele au doua propietati comune(nume si putere), dar si trei metode comune(>, lupta, _str_) ceea ce inseamna ca ar trebui sa existe o super clasa a tuturor claselor. Stabilim sa numim aceasta clasa Character.

## Raport tool AI

You
Comp Applic In Engineering - 2023 - Climent - Automatic assessment of object oriented programming assignments with unit.pdf
PDF
deci am de facut proiect pentru facultate la testarea sistemelor software si am de reprodus un studiu legat de asta pe cae l am gasit eu pe net, iti voi lasa documentul pdf ca sa l studiezi, eu am incercat sa fac ceva similar cu ce au facut oamenii respectivi in studiul lor. am construit urmatoarele clase: class Character: def __init__(self, name, strength): if not isinstance(name, str): raise TypeError("Name should be a string") if not isinstance(strength, float) and not isinstance(strength, int): raise TypeError("Strength should be a int") self._name = name self._strength = max(0, min(strength, 5)) @property def name(self): return self._name @name.setter def name(self, value): if not isinstance(value, str): raise ValueError("Name must be a string.") self._name = value @property def strength(self): return self._strength @strength.setter def strength(self, value): if not isinstance(value, (int, float)): raise ValueError("Strength must be a number.") if value < 0 or value > 5: raise ValueError("Strength must be between 0 and 5.") self._strength = value def __str__(self): return f"{self._name} {self._strength}" def __gt__(self, other): return self._strength > other.strength def fight(self, other): if self > other: self.strength = min(self.strength + 1, 5) print(f"{self.name} wins and now has strength {self.strength}") else: print(f"{other.name} wins and now has strength {other.strength}") from models.character import Character class Alien(Character): def __init__(self, name, strength, advancedTech): if not isinstance(advancedTech, bool): raise ValueError("Test that providing a non-boolean type for advancedTech raises an error") super().__init__(name, strength) self._advancedTech = advancedTech @property def advancedTech(self): return self._advancedTech @advancedTech.setter def advancedTech(self, value): if not isinstance(value, bool): raise ValueError("advancedTech must be a boolean value.") self._advancedTech = value def __str__(self): return f"{self.name} {self.strength} {'with' if self.advancedTech else 'without'} advanced technology" def __gt__(self, other): if isinstance(other, Alien) and self.advancedTech and not other.advancedTech: return True elif isinstance(other, Alien) and self.advancedTech == other.advancedTech: return self.strength > other.strength return self.strength > other.strength from models.character import Character class Human(Character): def __init__(self, name, strength, planet): if not isinstance(planet, str): raise TypeError("Planet should be a string") super().__init__(name, strength) self._planet = planet @property def planet(self): return self._planet @planet.setter def planet(self, value): if not isinstance(value, str): raise ValueError("Planet must be a string.") self._planet = value def __str__(self): return f"{self.name} from {self.planet} with strength {self.strength}" def fight(self, other): if isinstance(other, Human): print("Humans cannot fight among each other.") raise ValueError("Crew members must be from the same planet.") else: super().fight(other) from models.human import Human class Astronaut(Human): def __init__(self, name, strength, planet): super().__init__(name, strength, planet) def __str__(self): return f"Astronaut {self.name} from {self.planet} with strength {self.strength}" from models.astronaut import Astronaut from models.human import Human class Commander(Human): def __init__(self, name, strength, planet): super().__init__(name, strength, planet) self._crew = [] @property def crew(self): return self._crew @crew.setter def crew(self, new_crew): for member in new_crew: if not isinstance(member, Astronaut) or member.planet != self.planet: raise ValueError("All crew members must be Astronauts from the same planet as the commander.") self._crew = new_crew def add_crew_member(self, astronaut): if not isinstance(astronaut, Astronaut): raise ValueError("Only astronauts can be added to the crew.") if astronaut.planet != self.planet: raise ValueError("Crew members must be from the same planet.") self._crew.append(astronaut) def __str__(self): crew_names = ', '.join([astronaut.name for astronaut in self._crew]) return f"Commander {self.name} from {self.planet} with strength {self.strength} and with crew [{crew_names}]" eu ce vreau sa faci tu este sa studiezi pdf ul pe care ti l voi atasa si sa mi generezi teste unitare dupa modelul celor din studiu dar pentru clasele pe care ti le am dat eu


## ChatGPT

The study you provided discusses using unit testing for automatic assessment of OOP principles in student programming assignments. It specifically uses Python and its unittest library to create and execute tests. Here are examples of unit tests based on the study that you can adapt to your classes:
1. Testing Character class constructors and properties
This includes tests for correct initialization, type checking, and range enforcement for the attributes of the Character class.
import unittest
from models.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_initialization(self):
        char = Character("Hero", 4)
        self.assertEqual(char.name, "Hero")
        self.assertEqual(char.strength, 4)

    def test_character_strength_boundaries(self):
        char = Character("Hero", 6)
        self.assertEqual(char.strength, 5)
        char.strength = -1
        self.assertEqual(char.strength, 0)

    def test_invalid_type_name(self):
        with self.assertRaises(TypeError):
            Character(123, 3)

    def test_invalid_type_strength(self):
        with self.assertRaises(TypeError):
            Character("Hero", "strong")

if __name__ == '__main__':
    unittest.main()
2. Testing Alien and Human subclasses
Here, you can include tests to validate specific behaviors of these subclasses, such as the handling of additional attributes or overridden methods.
from models.alien import Alien
from models.human import Human

class TestAlienHuman(unittest.TestCase):

    def test_alien_technology(self):
        alien = Alien("Zorg", 3, True)
        self.assertTrue(alien.advancedTech)

    def test_invalid_alien_technology_type(self):
        with self.assertRaises(ValueError):
            Alien("Zorg", 3, "yes")

    def test_human_planet(self):
        human = Human("John Doe", 2, "Earth")
        self.assertEqual(human.planet, "Earth")

    def test_invalid_human_planet_type(self):
        with self.assertRaises(TypeError):
            Human("John Doe", 2, 404)
3. Testing interactions and behaviors
You can create unit tests for the interaction methods like fight() to ensure that characters behave correctly in simulated battles.
class TestCharacterInteraction(unittest.TestCase):

 
   def test_fight_winner(self):
        char1 = Character("Hero", 5)
        char2 = Character("Villain", 3)
        char1.fight(char2)
        self.assertEqual(char1.strength, 5)
        self.assertEqual(char2.strength, 3)  # Assuming fight logic in description

    def test_fight_strength_increase(self):
        char1 = Character("Hero", 4)
        char2 = Character("Villain", 3)
        char1.fight(char2)
        self.assertEqual(char1.strength, 5)  # Hero wins and gains strength

if __name__ == '__main__':
    unittest.main()
These tests should be a good starting point for building your test suite according to the principles discussed in the study you provided. They check for correct initialization, enforcement of attribute constraints, and proper method functioning, aligning with the study's methodology of using unit tests to validate OOP principles and class behaviors. Adjust the specific test logic based on the actual implementations and requirements of your fight() method or other class methods.


