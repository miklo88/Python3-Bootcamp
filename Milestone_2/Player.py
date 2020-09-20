# PLAYER CLASS -
'''
The last thing we need to think about is translating a Deck/Hand of cards with a top and bottom, to a Python list.
'''
class Player:
    def __init__(self, name):
        self.name = name 
        self.all_cards = []
    # now think of all the rules to the game. how will you write this out?

    # play a single card you pop off of the begining of a list
    #pop(0)
    def play_card(self):
        return self.all_cards.pop(0)
        # pass
    # adding a card to a list. append(goes to end of list)
    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            #for multiple cards
            self.all_cards.extend(new_cards)
        else:
            #single card object
            self.all_cards.append(new_cards)

    #adding multiple cards 
    # cards = cards in hand
    # new cards won
    # cards.extend(new) takes a list and mergest it with a new list

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
