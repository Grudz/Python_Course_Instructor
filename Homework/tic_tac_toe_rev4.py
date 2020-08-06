# Tic Tac Toe Homework - Ben Grudzien

import sys
from art import *

check_repeat_move = []

check_correct_answer = ['top-L', 'top-M', 'top-R',
                        'mid-L', 'mid-M', 'mid-R',
                        'low-L', 'low-M', 'low-R']

check_repeat_move_dict = {'top-L': 0, 'top-M': 0, 'top-R': 0,
                             'mid-L': 0, 'mid-M': 0, 'mid-R': 0,
                             'low-L': 0, 'low-M': 0, 'low-R': 0}
                        
                        

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def instructions():
    print('top-L | top-M | top-R')
    print('----- + ----- + -----')
    print('mid-L | mid-M | mid-R')
    print('----- + ----- + -----')
    print('low-L | low-M | low-R')
    print()


def check_O_winner(board):
    # Horizontal Wins
    if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()
    if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()
    if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()

    # Vertical Wins
    if board['low-L'] == 'O' and board['mid-L'] == 'O' and board['top-L'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()
    if board['low-M'] == 'O' and board['mid-M'] == 'O' and board['top-M'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()
    if board['low-R'] == 'O' and board['mid-R'] == 'O' and board['top-R'] == 'O':
        print("O Player WINS!!!")
        input()
        sys.exit()

    # Diagonal Wins
    if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()
    if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O':
        tprint("O Player WINS!!!")
        input()
        sys.exit()


def check_X_winner(board):
    # Horizontal Wins
    if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()
    if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()
    if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()

    # Vertical Wins
    if board['low-L'] == 'X' and board['mid-L'] == 'X' and board['top-L'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()
    if board['low-M'] == 'X' and board['mid-M'] == 'X' and board['top-M'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()
    if board['low-R'] == 'X' and board['mid-R'] == 'X' and board['top-R'] == 'X':
        print("X Player WINS!!!")
        input()
        sys.exit()

    # Diagonal Wins
    if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()
    if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
        tprint("X Player WINS!!!")
        input()
        sys.exit()        
  

tprint("TicTacToe.Py")
turn = 'X'
i = 0

for i in range(9): # 9 max moves
    
    repeat_check = 0
    
    print("\nTURN =", turn, "\n")
    if i < 1:
        print_board(board)
        i += 1

    check_O_winner(board)
    check_X_winner(board)
    
    print()
    print("Press [i] for instructions. Press [Enter] to continue")    
    user_selection = input()
    if user_selection == 'i':
        instructions() 
    
    print('Turn for ' + turn + '. Move on which space?')
    
    move = input()
    check_repeat_move.append(move)
    #print("Past Moves", check_repeat_move)
    check_repeat_move_dict.setdefault(move, 0)
    check_repeat_move_dict[move] += 1
    #print(check_repeat_move_dict)
    #print(check_repeat_move_dict.get(move, 0))
    if check_repeat_move_dict.get(move, 0) > 1:
        #print("repeat")
        repeat_check = 1

    #print(repeat_check)

    if move in check_correct_answer and repeat_check == 0:
        board[move] = turn
        
    while 1:
        if move in check_correct_answer and repeat_check == 0:
            break            
        print("Incorrect Input, try again")
        print("Press [i] for instructions. Press [Enter] to continue")
        user_selection = input()
        if user_selection == 'i':
            instructions()
        print('Turn for ' + turn + '. Move on which space?')
        move = input()

        check_repeat_move.append(move)
        #print("** Past Moves", check_repeat_move)
        check_repeat_move_dict.setdefault(move, 0)
        check_repeat_move_dict[move] += 1
        #print(check_repeat_move_dict)
        #print(check_repeat_move_dict.get(move, 0))
        if check_repeat_move_dict.get(move, 0) > 1:
            repeat_check = 1
            #print("** repeat")
        else:
            repeat_check = 0
            
        if move not in check_repeat_move and move in check_correct_answer:
            repeat_check = 0
        if move in check_correct_answer and repeat_check == 0 and move not in check_repeat_move:
            break 
        
    board[move] = turn
    print()
    print_board(board)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    if i == 8:
        tprint("Cat's Game")
    
                  




    
    



         
