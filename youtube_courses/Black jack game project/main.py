"""
DOCTYPE:
This will be a game implementing everything I've learned and can recap about Python today.
The link to the video is: https://www.youtube.com/watch?v=eWRfhZUzrAc&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB
time stamp for project start: 3:27:18

Check all the different versions on the github page because we are going to do a lot of refactoring for this project.
1. Beginning
2. Deck Class
3. Card Class
4. Hand Class
5. Game Class
6. Testing

and ofcourse cording to the description and message for each merge if a significant part of the program is finished.
"""
import random

# 1. 
cards = []
suits = ["spades", "clubs", "heart", "diamonds"]

# Notice the update to the rank list containing now dictionaries:
ranks = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
]

# fill the empty cards list with the deck and values stored in the ranks list:
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    # use the random library to shuffle the list of cards:
    random.shuffle(cards)


def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()

# get the value of each rank without using an if statement. Instead we'll store both rankName and value in the ranks list using dictionaries.

card = deal(1)[0]   # deal() returns a list. in this case containing one item since number = 1. [0] allows us to acces that first item.

print(card)