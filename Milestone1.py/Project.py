
#creating inputs as I talk myself throught the game.
#entering player details strings
# input(f'Welcome to tic tac toe! This game involves two players! Player 1 enter your name: ')
# input(f'Player 2 enter your name: ')

# #getting the game started
# instructions = '''Perfect! let's get to know how Tic Tac Toe work's here in python. You should see a blank
# board set up with three rows and three columns. To input your X or O you need to enter a number between 1-9.
# 1,2,3 starting at the bottom left, going right. Then 4,5,6 in the middle left working right and 7,8,9 on the
# top left working right. After you input your X or O then it will be the other players turn. 
# The game will end if you can align three in a row. Invalid entries are as such. "one", "five", "car", 10, 25,
# -4. Easy enought right?'''
# print(instructions)
# # string
# input(f'To start game type Y, or quit the best game ever before trying type N: ')

# #player picks marker
# input(f'Player 1 pick a marker X or O: ')
# #player inputs - ints
# player1 = int(input(f'Player 1 input: '))
# player2 = int(input(f'Player 2 input: '))

# #exiting the game - strings
# input(f'Congratulations you have won! Play again? Y or N:')
# input(f'Oh no! You lost! Welp what can you do? Play again Y or N?: ')
# # N = print('\n'*100)

#printing out the board.
def game_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    #test list
test_board = ['#','X','O','X','O','X','O','X','O','X']
game_board(test_board)

#player input
def player_input():
    #output is a tuple(Player 1 marker, Player 2 marker) this is what your output looks like
    marker = ''
    #ask player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
player1_marker, player2_marker = player_input()
# print(player1_marker)
# print(player2_marker)

#writing a function that takes in the board list object. (x or o) and a position number and assigns it
# to the board.
def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board, '&', 4)
game_board(test_board)

def win_check(board, mark):
    #WIN TIC TAC TOE?
    #ALL ROWS, and check to see if they all share the same marker
    (board[1] == mark and board[2] == mark and board[3] == mark ) or
    (board[4] == mark and board[5] == mark and board[6] == mark ) or
    (board[7] == mark and board[8] == mark and board[9] == mark ) or
    #columns
    (board[1] == mark and board[2] == mark and board[3] == mark ) or
    (board[4] == mark and board[5] == mark and board[6] == mark ) or
    (board[7] == mark and board[8] == mark and board[9] == mark ) or
    #diagonal
    (board[1] == mark and board[5] == mark and board[9] == mark ) or
    (board[3] == mark and board[5] == mark and board[7] == mark )
    #ALL COLUMNS, check to see if the marker matches
    #2 diagonals, check to see match