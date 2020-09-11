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
import random
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
#card class attributes defined as global values above. creats a card with a suit,rank,value. ex. 
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Deck class - three things. 1)instantiate a new deck a.create all 52 card objects b.hold as a list of card objects.
# 2) shuffle a deck through a method call a.random library shuffle() function. 3) deal cards from the deck object a.pop method from cards list 
class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create a card object.
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
#now we created a deck, now its time to shuffle this deck.
    def shuffle(self):
        #be mindful random.shuffle technically returns nothing.
        # shakey shakey shakey
        random.shuffle(self.all_cards)

    # dealing cards meow
    #can do more like splitting deck in half, or deal multiple cards.
    # for right now we only need to deal one. could have multiple functions and multiple inputs for invoking them. 
    def deal_one(self):
        return self.all_cards.pop()

    # def __str__(self):
    #      print(f'The Deck class : {created_card}')

#deck class
new_deck = Deck()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]

# prints deck
for card_object in new_deck.all_cards:
    print(card_object)

print(f'Last Card : {last_card}')
# print(new_deck.all_cards[0])
print(f'First Card : {first_card}')
new_deck.shuffle()
print("'shuffle' 'shuffle' 'shuffle'")
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(f'Last Card : {last_card}')
# print(new_deck.all_cards[0])
print(f'First Card : {first_card}')
mycard = new_deck.deal_one()
print(mycard)
print(len(new_deck.all_cards))
# print(new_deck.all_cards)s
# card class
# card = Card('Hearts','Jack')
# print(card)
# print(card.suit)
# print(card.rank)
# print(card.value)
# print(values[card.rank])
# print(values[card.suit])

# print(len(suits))
# print(suits[0])
# print(suits[1])
# print(suits[2])
# print(suits[3])