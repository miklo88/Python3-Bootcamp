import random

#printing out the board.
def game_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    #test list
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# game_board()

#player input
def player_input():
    #output is a tuple(Player 1 marker, Player 2 marker) this is what your output looks like
    marker = ''
    #ask player 1 to choose X or O
    while (marker != 'X' and marker != 'O'):
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
# player1_marker, player2_marker = player_input()
# print(player1_marker)
# print(player2_marker)

#writing a function that takes in the board list object. (x or o) and a position number and assigns it
# to the board.
def place_marker(board, marker, position):
    board[position] = marker
# place_marker()
# place_marker(test_board, '&', 4)
# game_board()

def win_check(board, mark):
    #WIN TIC TAC TOE?
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    #columns
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    #diagonal
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))
# game_board(test_board)
# win_check()
#Writing a function that uses the random module to randomly decide which player goes first.
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
# choose_first()
#a function to see if a space in the board is available
def space_check(board, position):
    return board[position] == ' '
# space_check()
#write a function and check if the board is full and returns a boolean value.
#True if full, false for otherwise
def full_board_check(board):
    for i in range(1,10):
        #if i have a space the board is not full and i'll return false
        if space_check(board,i):
            return False
            #board is full if we return true
        return True
# full_board_check()
# ask for a players next position. then uses the function from space_check to see if the space is available 
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position
# player_choice()
#ask player if they want to play again
def replay():
    choice = input(f'Play again? Enter Yes or No: ')

    return choice == 'Yes'


#while loop to keep running the game
print("Welcome to Tic Tac Toe")

while True:
    #play the game
#set up BOARD, WHOS FIRST, CHOOSE MARKERS
#game play, player one turn, player two turn
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    #who goes first
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    #gameplay
    while game_on:
        if turn == 'Player 1':
            game_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #place marker on a position
            place_marker(theBoard, player1_marker, position)
            #check if they won
            if win_check(theBoard, player1_marker):
                game_on(theBoard)
                print('Player 1 has total victory!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    game_board(theBoard)
                    print("Tie Game")
                    break
                else:
                    turn = 'Player 2'

        else:
            #player 2 turn
            game_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #place marker on a position
            place_marker(theBoard, player2_marker, position)
            #check if they won
            if win_check(theBoard, player2_marker):
                game_board(theBoard)
                print('Player 2 has total victory!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    game_board(theBoard)
                    print("Draw")
                    break
                else:
                    turn = 'Player 1'
            #or check if there is a tie
            #no tie and no win, then next players turn
    if not replay():
        break
#break out of loop 
print(3+5)
