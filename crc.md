So in my pig module I have created three classes:

class Die

class Player

class Computer

class Game

These are the responsibilities for each class:

class Die
    -give a random number between one and six

class Player
    -decide whether player is hitting or hold (this will be an input)
    -returns either hit or hold
    -hold players total score

class Computer
    -continues to hit until its current round score is >= 20
    -hold computers total score

class Game
    -decide who gets to go first
    -play a round with player one, then continue on to player two
        round:
        -immediately hit once
        -show score
        -ask whether to hit again
        -repeat until role = 0 OR player says to lock it in
    -continue until one score equals 100