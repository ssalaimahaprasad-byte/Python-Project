# 🛡️ Gladiator Battle Game (Python OOP)

A simple command-line Gladiator Battle Game developed in Python to demonstrate Object-Oriented Programming (OOP) concepts such as inheritance, method overriding, nested classes, exception handling, and class variables.

## 📌 Features

- Create Gladiator and Warrior characters
- Weapon system with damage and durability
- Battle simulation between two players
- Custom exception for broken weapons
- Automatic winner declaration
- Demonstrates core Python OOP concepts

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

## 📂 Project Structure

```
project/
│── battle_game.py
│── README.md
```

## 🚀 OOP Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Method Overriding
- Nested (Inner) Classes
- Class Variables
- Exception Handling
- Custom Exceptions
- `super()` Method

## 🎮 How the Game Works

1. Two gladiators are created.
2. Each gladiator has:
   - Name
   - Health Points (HP)
   - Weapon
3. Every attack:
   - Reduces the opponent's HP.
   - Decreases weapon durability.
4. When weapon durability becomes zero:
   - A custom `WeaponBreakError` is raised.
   - The Warrior switches to a normal punch attack.
5. The battle continues until one player's HP reaches zero.
6. The remaining player is declared the winner.

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/gladiator-battle-game.git
```

Go to the project folder:

```bash
cd gladiator-battle-game
```

Run the program:

```bash
python battle_game.py
```

## 📖 Sample Output

```
Battle Begins!

Hercules attacks Maximus with Spear
Maximus HP: 85

Maximus attacks Hercules with Sword
Hercules HP: 90

Weapon Broken!
Hercules punches Maximus.

Winner: Hercules
```

## 📚 Learning Outcomes

This project helps understand:

- Python Classes
- Object Creation
- Inheritance
- Method Overriding
- Exception Handling
- Custom Exceptions
- Class Variables
- Nested Classes
- Game Logic Implementation

## 🔮 Future Enhancements

- Add multiple gladiators
- Add different weapon types
- Special attack abilities
- Health potions
- Scoreboard
- Graphical User Interface (Tkinter/Pygame)
- Multiplayer mode

## 👨‍💻 Author

**Salai Mahaprasad**

Bachelor of Engineering (Computer Science and Engineering)

## 📄 License

This project is created for learning and educational purposes.
