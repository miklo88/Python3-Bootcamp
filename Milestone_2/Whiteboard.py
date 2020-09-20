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


while len(whiteboard_Deck.all_cards) < 52:
    # print(len(W_Deck_1))
    # W_Deck_1 += 1
    whiteboard_Deck.shuffle()
    
    for i in whiteboard_Deck.all_cards:
        # print(i)

        if len(player_1.all_cards) < 26: 
            player_1.add_card(i)

        # print('Ones Cards: ', player_1.all_cards)
        elif len(player_2.all_cards) < 26:        
            player_2.add_card(i)
        else:
            print('done dealing')

    break
    print(player_1.all_cards)
    print(player_2.all_cards)
else:
    print("Deck has been dealt")
#     if whiteboard_Deck.all_cards == 52:
#         break
#     whiteboard_Deck.all_cards += 1
    
    # else:
    #     print('All cards dealt')
    #     break


