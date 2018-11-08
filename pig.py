import random

class Die:
    "Gives out the random dice roll every time it's called."

    def __init__(self):
        pass

    def dice_roll(self):
        return random.randint(1, 6)

class Player(self, total_score):
    
    def __init__(self, total_score):
        self.total_score = 0

    def add_to_player(self, points_to_add):
        self.total_score += points_to_add

    def hit_or_hold(self):
        choice = input(f'Your turn total is {turn_total} Would you like to hit again (y) or no (n)')
        if choice == 'y'
            return True
        else:
            return False
    
class Computer:

    def __init__(self, total_score):
        self.total_score = 0

    def add_to_computer(self, points_to_add):
        self.total_score += points_to_add
    
    def hit_or_hold(self):
        if points_to_add <= 20
            return True
        else:
            return False

class Game:

    def __innit__(self, player_one, player_two, dice_roller,):
        self.random_start = random.randint(1, 2)
        self.player_one = player_one
        self.player_two = player_two
        self.player_counter = 0
        self.dice_roller = self.die.dice_roll

    def who_starts_first(self):
        if self.random_start == 1:
            return "Player One Starts"
        else:
            return "Player Two Starts"

    def round(current_player):
        round_score = 0
        current_player()
        points = self.die.roll() '''this score is between 1 and 6'''
            while points is not 1 self.hit_or_hold is true:
                if current_player rolls dice:
                    add points to round_score
                    prompt hit_or_hold
                    continue
            if points == 1:
                print total_score
            """when loop ends"""
            if current_player == player_one
                player_counter += 1
             if current_player == player_two
                player_counter -= 1



