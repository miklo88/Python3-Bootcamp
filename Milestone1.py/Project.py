'''
-------------------------------First Milestone Project.
Tic Tac Toe for 2 players
1)2 players should be able to play the game
(Both sitting at the same computer)
2)The board should be printed out every time a player makes a move
3)You should be able to accept input of the player position and then place a symbol on the board.

-------------------------------lets break these down into smaller problems
#####gotta create an input and filter what the users input. user interface.
datatype needed will be an int. 

#####gotta create two states for players. how do i update their status?
player 1
player 2

#####gotta create a board to play on
use the numpad to match numbers to the grid on a tic tac toe board:
[789]
[456]
[123]
now how am i going to visualize a gameboard and how will i be able to get x's and o's into this gameboard. 
how do i get three lists to read up/down/left/right/diagonally?

#####gotta be able to update that board. then when three in a row occur end game. or if all fills up
and no matches the game is a draw.
if three x's end game
if three o's end game but how do i do that diagonally??
tie game is full board no matches.

#####gotta create dialog for users in the game. 
# if you win -congrats, if you lose, well -its ok. a sequence for quitting mid game-you mad bro?.
do you want to play again? Yes or No.

-------------------------------quick rundown
this is the layout for our x's and o's

how do i get a user to understand what number to input for their x or o input.
check to see if someone has won or tied.

#####quick peek at game
on start
player 1: do you want to be x or o?
think of battleship for player input.
Do you want to play again? yes or no? If yes, play again, if no show messages for win, loss, or not finished.
##
'''
#creating inputs as I talk myself throught the game.
#entering player details
input(f'Welcome to tic tac toe! This game involves two players! Player 1 enter your name: ')
input(f'Player 2 enter your name: ')
#getting the game started
instructions = '''Perfect! let's get to how Tic Tac Toe work's here in python. You should see a blank
board set up with three rows and three columns. To input your X or O you need to enter a number between 1-9.
1,2,3 starting at the bottom left, going right. Then 4,5,6 in the middle left working right and 7,8,9 on the top left 
working right. After you input your X or O then it will be the other players turn. 
The game will end if you can align three in a row. Invalid entries are as such. "one", "five", "car", 10, 25, -4. Easy enought right?'''
print(instructions)
input(f'To start game type Yes, or quit the best game ever type No.: ')

#player inputs 
input(f'Player 1 input: ')
input(f'Player 2 input: ')