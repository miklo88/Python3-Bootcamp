
#creating inputs as I talk myself throught the game.
#entering player details strings
input(f'Welcome to tic tac toe! This game involves two players! Player 1 enter your name: ')
input(f'Player 2 enter your name: ')

#getting the game started
instructions = '''Perfect! let's get to know how Tic Tac Toe work's here in python. You should see a blank
board set up with three rows and three columns. To input your X or O you need to enter a number between 1-9.
1,2,3 starting at the bottom left, going right. Then 4,5,6 in the middle left working right and 7,8,9 on the
top left working right. After you input your X or O then it will be the other players turn. 
The game will end if you can align three in a row. Invalid entries are as such. "one", "five", "car", 10, 25,
-4. Easy enought right?'''
print(instructions)
# string
input(f'To start game type Y, or quit the best game ever before trying type N: ')

#player picks marker
input(f'Player 1 pick a marker X or O: ')
#player inputs - ints
player1 = int(input(f'Player 1 input: '))
player2 = int(input(f'Player 2 input: '))

#exiting the game - strings
input(f'Congratulations you have won! Play again? Y or N:')
input(f'Oh no! You lost! Welp what can you do? Play again Y or N?')