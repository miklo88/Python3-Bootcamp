import random
from Card import Card, Deck
from Player import Player

player_1 = Player('One')
player_2 = Player('Two')

print('Hola!!!!!', player_1)
print('Hello', player_2)
whiteboard_Deck = Deck()
print('Whiteboard deck: ', whiteboard_Deck)

# prints card objects...
# print(W_Deck_1)
# prints individual card.
# print(W_Deck_1[0])
# for i in range(W_Deck_1):
    # print(i)

    # print(len(W_Deck_1))
    # W_Deck_1 += 1
whiteboard_Deck.shuffle()
# i = whiteboard_Deck
i = 1
while i < len(whiteboard_Deck.all_cards):
    # print(i)

    if len(player_1.all_cards) < 26: 
        player_1.add_card(i)
        i += 1
        # print('Ones hand: ', player_1.all_cards)
        
        # print('Ones Cards: ', player_1.all_cards)
    elif len(player_2.all_cards) < 26:        
        player_2.add_card(i)
        i += 1
        # print('Twos hand: ', player_2.all_cards)
    else:
        print('re-deal')
        break

# PLAYER ONE
# print(player_1.all_cards)
print('First Card', player_1.all_cards[0])
print('Last Card', player_1.all_cards[-1])
print('Card played', player_1.play_card())

# PLAYER TWO
# print(player_2.all_cards)
print('First Card', player_2.all_cards[0])
print('Last Card', player_2.all_cards[-1])
print('Card played', player_2.play_card())

#WARRRRRRRRRRRR
# if one players card is greater in value than the other. then you keep their card.
if player_1.play_card() > player_2.play_card():
    player_1.add_card(player_2.play_card())
# if we have equal values. we must draw two more times. 
else:
    print('something went wrong.')
# anything else would be iteration of the sequence of equal cards. or the other player winning. 



