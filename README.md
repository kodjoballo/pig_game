# 🐷 Pig Dice Game

### 📌 Description
A simple implementation of the **Pig dice game** in Python.  
Players take turns rolling a six-sided dice. Each roll adds to their score, **unless** they roll a `1`.  
If they roll a `1`, they **lose all points for that turn** and their turn ends.  
The first player to reach **50 points** wins! 🎉  

---

### 🚀 How to Run
```js
python.exe pig.py
```

or run using any python interpreter

### 🎮 Rules of the Game

Choose the number of players (2–4)

On a player’s turn, they keep rolling the dice until they decide to stop or roll a 1

If they roll a 1, they lose their turn score and end their turn immediately

The first player to reach 50 points wins

### 📚 Concepts Used

Random number generation with random.randint()

Loops & conditionals to control gameplay

Lists to store player scores

Input validation

### 🖼️ Example Output

```js

******************
**** PIG GAME ****
******************

Pick a number between 2-4 for the number of players to play: 3

number of player selected : 3

Turn of player 1
score: 0
Do you wanna roll ? (Y) : y
You have rolled 5
total : 5
Do you wanna roll ? (Y) : y
You have rolled 3
total : 8
Do you wanna roll ? (Y) : y
You have rolled 1!!!!
Turn done

Player 1, score: 8

Turn of player 2
score: 0
...
Player number 3 is the winner with the score 52

```

<p align="center">

![image alt](https://github.com/kodjoballo/pig_game/blob/main/pig.png?raw=true)

</p>

### 💡 Ideas to Extend

Add a “Hold” option so players can stop rolling and keep their score safely

Allow the winning score to be configurable instead of fixed at 50

Add computer opponents with simple AI strategies

Create a GUI version using Tkinter or Pygame

### code source ☺️👇

[code source](https://github.com/kodjoballo/pig_game/blob/main/pig.py)
