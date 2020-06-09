'''
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
'''
'''
First, pick a random integer from 1 to 100 using the random module and assign it to a variable
Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.
'''
from random import randint
randomnumber = randint(1,100)
print(randomnumber)
'''
Next, print an introduction to the game and explain the rules
'''
print("You must guess a number between 1 and 100!")
print("If you are close i'll let you know you're warm")
print("If you are really close i'll say you're WARMER")
print("If you are kind of close i'll say you're cool")
print("If you are in another atmosphere i'll say you're COLDER")
print("If you're on the money i'll say HELURR")

'''
Create a list to store guesses
Hint: zero is a good placeholder value. It's useful because it evaluates to "False"
Write a while loop that asks for a valid guess. Test it a few times to make sure it works.
'''
guesses = [0]
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess? "))
    if guess < 1 or guess > 100:
        print('no no no, out of bounds. Please try again: ')
        continue
    #comparing the players guess to our number
    if guess == randomnumber:
        print(f'Congratulations, you guessed it in only {len(guesses)} guesses!')
        break
#if guess is incorrect add it to the list
    guesses.append(guess)

    #when testing the first guess, guesses[-2]==0, which evaluates to False
    #and brings us down to the second section
    if guesses[-2]:
        if abs(randomnumber-guess) < abs(randomnumber-guesses[-2]):
            print("Warmer")
        else:
            print("Colder")
    else:
        if abs(randomnumber-guess) <= 10:
            print("Warm")
        else:
            print("Cold")

'''
Write a while loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
Some hints: [
it may help to sketch out all possible combinations on paper first!
you can use the abs() function to find the positive difference between two numbers
if you append all new guesses to the list, then the previous guess is given as guesses[-2]]
'''

'''
That's it! You've just programmed your first game!

In the next section we'll learn how to turn some of these repetitive actions into functions that can be called whenever we need them.
'''