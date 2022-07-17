#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time
import string 

moves = ['rock', 'paper', 'scissors']

def print_pause(message_to_print, delay=1):
    typewriter_simulator(message_to_print)
    time.sleep(delay)


def typewriter_simulator(message_to_print):
    for char in message_to_print:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')

    
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'The option "{option}" is wonky. Try again!')


class Player:
    score = 0
    my_move = None
    their_move = None   

    def learn(self, my_move, their_move):
        pass


class AllRock(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):        
    def move(self, moves):
        return random.choice(moves)

            
class HumanPlayer(Player):              
    def move(self):
        return valid_input("Choose rock, paper, or scissors:\n", moves)


class ReflectPlayer(Player):
    def move(self):
        return random.choice(moves)
    
    def learn(self, my_move, their_move):
        self.my_move = their_move
     

class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        index = moves.index(self.my_move) + 1
        if index % len(moves) == 0:
            index = 0
        return moves[index]
    
    def learn(self, my_move, their_move):
        self.my_move = my_move

def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

class Game:
    p1_score = 0
    p2_score = 0
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        
        print(f"Player 1: {move1} Player 2: {move2}")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == move2:
            print_pause("Tie Game!")
        elif beats(self, move1, move2):
            self.p1.score += 1
            print("Player 1 wins!")
        else:
            self.p2.score += 1
            print("Player 2 wins!")
        
        
        print_pause("Scores: ")
        print_pause(f"Player 1: {self.p1.score}")
        print_pause(f"Player 2: {self.p2.score}")


    def play_game(self):
        print_pause("Game start!")
        for round in range(1, 4):
            print_pause(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print_pause("The winner is Player 1!")
        elif self.p1.score < self.p2.score:
            print_pause("The winner is Player 2!")
        else:
            print_pause("Tie Game!")

        print_pause("Game over!")


if __name__ == '__main__':
    opponents = [
        AllRock(),
        RandomPlayer(),
        CyclePlayer(),
        ReflectPlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(opponents)
    game = Game(p1, p2)
    game.play_game()
