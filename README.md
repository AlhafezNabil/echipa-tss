# TSS-Project



### [Articol original](https://onlinelibrary.wiley.com/doi/10.1002/cae.22642)


### [DEMO](https://youtu.be/g8Dw-8hYT6w)

 # Evaluarea automată a principiilor de OOP și Testare unitară în Python

 În cadrul acestei lucrări, ne concentrăm pe dezvoltarea unei metode de evaluare automată (AA) pentru un domeniu care prezintă unele provocări în evaluarea sa practică: programarea orientată pe obiecte (OOP). Pentru a evalua corectitudinea aplicării principiilor OOP într-o aplicație reală, ne folosim de testarea unitară. 
 Chiar dacă alte limbaje au framework-uri de testare bine stabilite, programarea orientată pe obiecte variază în funcție de specificul limbajului și de nevoile utilizatorilor. Un studiu de caz pe această temă permite adaptarea și rafinarea testelor la mediul particular în care sunt folosite.
	Testele unitare pot fi construite în mod specific pentru a aborda nevoile și problemele întâlnite de studenții sau dezvoltatorii care utilizează un limbaj particular. Acest lucru duce la o îmbunătățire a procesului de învățare și asigură dezvoltarea abilităților practice.
	Deși alte limbaje pot avea deja metode standardizate de testare, fiecare limbaj de programare are particularități unice care necesită abordări personalizate. Articolul poate demonstra eficiența testării automate în limbajul respectiv, oferind exemple relevante pentru comunitatea dezvoltatorilor.

## Scopul Lucrării

Accentul este pus pe încurajarea elevilor să înțeleagă și să aplice corect principiile OOP complexe, precum și pe capacitatea lor de a proiecta în mod adecvat clasele și relațiile dintre acestea. În acest sens, prezentăm un studiu de caz bazat pe o sarcină practică, în care elevii sunt solicitați să creeze personaje pentru un joc video. Această sarcină este remarcabilă prin faptul că este incrementală și abordează toate cele patru principii OOP într-un singur context.

## De ce este importanta aceasta lucrare:
Studiul pe care l-am ales, [Automatic Assessment of Object-Oriented Programming Assignments with Unit Testing in Python](https://onlinelibrary.wiley.com/doi/10.1002/cae.22642) de Laura Climent și Alejandro Arbelaez, este interesant și util în contextul testării unitare, din mai multe motive:

1. Relevanță în lumea reală: Studiul abordează o problemă practică din programarea orientată pe obiecte (OOP), respectiv implementarea unor personaje de joc video. Astfel, studenții își pot aplica cunoștințele teoretice la provocări de codare reale, ceea ce face testarea mai relevantă.

2. Acoperire cuprinzătoare a principiilor OOP: Evaluarea include toate cele patru principii de bază OOP: încapsularea, abstractizarea, moștenirea și polimorfismul. Abordarea incrementală permite studenților să înțeleagă și să aplice aceste concepte în mod gradual.

3. Orientare specifică spre Python: În timp ce multe lucrări anterioare se concentrează pe Java, studiul de față pune accent pe Python, reflectând popularitatea sa în creștere. Autorii folosesc biblioteca unittest, ceea ce face ca materialul să fie aplicabil direct pentru studenții și instructorii care lucrează cu acest limbaj.

4. Evaluare automată: Automatizarea procesului de evaluare reduce timpul necesar pentru corectarea manuală, oferind în același timp feedback consistent. Acest lucru este important mai ales pentru cursurile mari sau pentru cele online, unde feedback-ul personalizat este dificil de oferit.

5. Evaluare și soluții detaliate: Autorii includ o diagramă UML, exemple practice de cod și îndrumări pentru testarea unitară, ajutând instructorii să înțeleagă structura temelor și oferind studenților feedback cuprinzător.

6. Rezultate de învățare eficiente: Evaluările pozitive ale studenților și comparația dintre evaluările automate și cele manuale arată că automatizarea se aliniază bine cu evaluarea umană, întărind credibilitatea acestui proces.

Acest studiu este interesant deoarece oferă un cadru solid care leagă învățarea teoretică de cea practică pentru OOP, în timp ce pune accent pe un limbaj de programare tot mai popular. Abordarea este practică pentru instructorii care doresc să evalueze în mod consistent concepte complexe.

## Cele Patru Principii de OOP

1. **Încapsularea:** constă în gruparea datelor și metodelor conexe într-o singură entitate (clasa). Încapsularea permite, de asemenea, ca codul să fie legat liber.
2. **Abstracția:** permite ascunderea membrilor, metodelor și implementării în interiorul clasei.
3. **Moștenirea:** este un principiu foarte util al OOP care construiește relații între clase. 
4. **Polimorfismul:** înseamnă că o metodă poate face față diferitelor tipuri de intrări.

## Studiu de Caz: Implementarea personajelor unui joc video

Prezentăm un studiu de caz real al unei aplicații OOP — „Implementarea personajelor unui joc video, Supraviețuirea în Cosmos” — care aplică toate cele patru principii OOP pentru a rezolva acest singur scenariu.

### Clasa Alien

#### Atribute:
- `name`: nume alien (ex: “Zyglorx”)
- `strength`: nivel de forță [0-5]
- `advancedTech`: are tehnologie avansată [True/False]

#### Metode asociate:
1. Constructor pentru inițializare
2. Proprietăți de accesare și modificare a valorilor tuturor
3. Metoda `__str__`
4. Supraîncărcarea operatorului `>`
5. Metoda `fight`

## Testarea și Gestionarea erorilor

Scopul nostru este să implementăm atât teste pentru gestionarea erorilor de tipuri și valori pentru atributele clasei, dar și pentru verificarea tuturor funcționalităților clasei Alien.

## Observații finale

În aplicația noastră, nu avem doar clasa Alien, ci și alte clase precum Astronaut și Commander, care împărtășesc anumite caracteristici și metode. 


 ## Diagrama UML
![image](https://github.com/AlhafezNabil/echipa-tss/assets/94968546/f57f33ee-88c4-4048-851f-800396da0d90)


## Raport AI
# Evaluarea automată a sarcinilor de programare orientată pe obiecte cu teste unitare

Acest proiect își propune să reproducă un studiu privind evaluarea automată a sarcinilor de programare orientată pe obiecte (OOP) utilizând teste unitare, așa cum se găsește în documentul PDF furnizat. Accentul este pus pe implementarea testelor unitare pentru clasele Python pentru a evalua aplicarea corectă a principiilor OOP.

## Prezentare generală

Studiul discută despre utilizarea testării unitare pentru evaluarea automată a principiilor POO în temele de programare ale elevilor. Utilizează în mod specific Python și biblioteca sa unittest pentru a crea și executa teste.

## Running Tests
- Ensure functionality by running unit tests structured in the tests directory. Execute the following command in the root directory:   
`python -m unittest discover -s tests`

## Implemantare

```python
class Character:
    def __init__(self, name, strength):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        if not isinstance(strength, float) and not isinstance(strength, int):
            raise TypeError("Strength should be a int")
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

class Human(Character):
    def __init__(self, name, strength, planet):
        if not isinstance(planet, str):
            raise TypeError("Planet should be a string")
        super().__init__(name, strength)
        self._planet = planet

    @property
    def planet(self):
        return self._planet

    @planet.setter
    def planet(self, value):
        if not isinstance(value, str):
            raise ValueError("Planet must be a string.")
        self._planet = value

    def __str__(self):
        return f"{self.name} from {self.planet} with strength {self.strength}"

    def fight(self, other):
        if isinstance(other, Human):
            print("Humans cannot fight among each other.")
            raise ValueError("Crew members must be from the same planet.")
        else:
            super().fight(other)

class Astronaut(Human):
    def __init__(self, name, strength, planet):
        super().__init__(name, strength, planet)

    def __str__(self):
        return f"Astronaut {self.name} from {self.planet} with strength {self.strength}"

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
```


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
