# -*- coding: utf-8 -*-
import random
from random import choice #imports random choice function

play_again = 'y'
comp_score = 0
human_score = 0
    
while play_again == 'y':
    moves = ['rock','paper','scissors']
    comp_move = random.choice(moves)
    
    print("Make a move! (r/s/p)")
    player_move = input()
    if player_move == 'r':
        player_move = "rock"
    elif player_move =='s':
        player_move = "scissors"
    else:
        player_move = "paper"
        
    if player_move == comp_move:
        results = "draw"
    elif player_move == "rock" and comp_move == "paper" or player_move == "paper" and comp_move == "scissors" or player_move == "scissors" and comp_move == "rock":
        results = "lose"
    else:
        results = "win"
        
    print("You chose", player_move, "and computer chose", comp_move, "you", results+"!")

    if results =="win":
        human_score = human_score + 1
    if results == "lose":
        comp_score = comp_score + 1
    get_score = input()
    if get_score == "sc":
        print ("human:", human_score, "computer:", comp_score)
    
    print("Do you want to play again? (y/n)")
    play_again = input()
    if play_again == "n":
        print("Thanks bye!")

        
        
        
    
        
            