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

from Card import Card, Deck
from Player import Player


#deck class
new_deck = Deck()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]

# prints deck
# for card_object in new_deck.all_cards:
#     print(card_object)
print("Dealing/shuffling the deck")
print(f'Last Card : {last_card}')
# print(new_deck.all_cards[0])
print(f'First Card : {first_card}')
new_deck.shuffle()
print("'shuffle' 'shuffle' 'shuffle'")
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
# print(f'Last Card : {last_card}')
# # print(new_deck.all_cards[0])
# print(f'First Card : {first_card}')
mycard = new_deck.deal_one()

# your_hand = []
# your_hand.append(mycard)

# print('Your hand:', your_hand[0])
print('my card:', mycard)
print('Cards left in deck', len(new_deck.all_cards))

# Player class
new_player = Player('Carlitos')
# player.name()
print(new_player)
new_player.add_card([mycard,mycard,mycard])
print(new_player)
print(f'Players Hand: {new_player.all_cards}')
# print(new_player.all_cards[1])
# print(new_player.all_cards[2])
print(f'Card Played: {new_player.play_card()}')
print(new_player)
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