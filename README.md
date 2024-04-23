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
