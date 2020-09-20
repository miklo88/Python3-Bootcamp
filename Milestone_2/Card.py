import random
#Card Class
'''
#card class attributes defined as global values above. creats a card with a suit,rank,value. ex. 
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

# CARD CLASS
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#DECK CLASS
'''
# Deck class - three things. 1)instantiate a new deck a.create all 52 card objects b.hold as a list of card objects.
# 2) shuffle a deck through a method call a.random library shuffle() function. 3) deal cards from the deck object a.pop method from cards list 
'''
class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create a card object. Card class aqui
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
