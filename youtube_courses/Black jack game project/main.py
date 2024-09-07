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
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
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
