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

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
   
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
        
    def move(self, moves):
        print_pause(random.choice(moves))
    
    def learn(self, my_move, their_move):
        for my_move in moves:
            self.move(moves)
        for their_move in moves:
            self.move(moves)   

            
class HumanPlayer(Player):              
    def move(self, moves):
        human_move = input("Choose rock, paper, or scissors:\n")
        while human_move.lower() not in moves:
            print_pause("That is not a valid choice. Try again!")
            human_move = input("Choose rock, paper, or scissors:\n")
        return human_move


class ReflectPlayer(Player):
    def move(self, moves):
        print_pause(random.choice(moves)
    
    def learn(self, my_move, their_move):
        self.their_move = their_move
     

class CyclePlayer(Player):
    def move(self, moves):
        self.my_move = random.choice(moves)
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"
    
    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    
    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


    def play_round(self):
        move1 = self.p1.move(moves)
        move2 = self.p2.move(moves)
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2) is True:
            self.p1score += 1
            print_pause("Player 1 wins!")
        elif self.beats(move2, move1) is True:
            self.p2score += 1
            print_pause("Player 2 wins!")
        else:
            print_pause("Tie Game!")
               
        for score in range(1, 4):
            print_pause("Scores: ")
            print_pause(f"Player 1: {self.p1score}")
            print_pause(f"Player 2: {self.p2score}")
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
            
            

    def play_game(self):
        print_pause("Game start!")
        for round in range(1, 4):
            print_pause(f"Round {round}:")
            self.play_round()
        print_pause("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
