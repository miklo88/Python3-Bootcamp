'''
Creating war the card game in python!

Deck of 52 cards
shuffle then deal 2 ways equally 26 
players draw a card face down from their stack and present them to each other.
the player with the higher card wins the round and collects the other players card.
if the cards are the same values, each player draws another card but doesn't present.
then draws another card to present. 
if draw again, keep repeating until winner.

when one player has collected all the cards they have won.

you will create with OOP
and classes being connected to other classes.
card class
deck class - has card class inheritence
player class
game logic

building the classes out here first.

'''
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14,
}
#card class attributes defined as global values above.
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

    

card = Card('Hearts','Jack')
print(card)
print(card.suit)
print(card.rank)
print(card.value)
# print(values[card.rank])
# print(values[card.suit])

print(len(suits))
print(suits[0])
print(suits[1])
print(suits[2])
print(suits[3])