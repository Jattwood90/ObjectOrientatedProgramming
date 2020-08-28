import random

#Global variables for Card class
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
              'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
              'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')

#Game start variables
print('Welcome to war! Player one please input your name: ', end='')
One = str(input())

print('and Player Two: ', end='')
Two = str(input())

#Difficulty setting
def levelSelect():
    while True:
        level = int(input())
        if level <=2 or level >=11:
            print('Please select a level in range 3 - 10.')
        else:
            return level

print('Input the number of cards you wish to use. The more cards, the quicker the game (3 - 10): ', end='')
level = levelSelect()
print(f'{level} selected!')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

    def dealCard(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def removeCard(self):
        return self.all_cards.pop(0)

    def addCard(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



player_one = Player(One)
player_two = Player(Two)

new_deck = Deck()
new_deck.shuffle()

for items in range(26):
    player_one.addCard(new_deck.dealCard())
    player_two.addCard(new_deck.dealCard())

game_on = True

round = 0

while game_on:
    round +=1
    print(f'Round {round}')

    #winning cases
    if len(player_one.all_cards) == 0:
        print(f'{One} has lost!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{Two} has lost!')
        game_on = False
        break

    #New round
    player_one_cards = []
    player_one_cards.append(player_one.removeCard())

    player_two_cards = []
    player_two_cards.append(player_two.removeCard())

    #War conditions

    at_war = True

    while at_war:

        if player_one_cards[-1].value >  player_two_cards[-1].value:
            player_one.addCard(player_one_cards)
            player_one.addCard(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value <  player_two_cards[-1].value:
            player_two.addCard(player_one_cards)
            player_two.addCard(player_two_cards)

            at_war = False

        else:
            print('War declared!')
            if len(player_one.all_cards) < level:
                print(f'{One} unable to play')
                print(f'{Two} wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < level:
                print(f'{Two} unable to play')
                print(f'{One} wins!')
                game_on = False
                break

            else:
                for num in range(level):
                    player_one_cards.append(player_one.removeCard())
                    player_two_cards.append(player_two.removeCard())
