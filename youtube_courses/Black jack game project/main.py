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

class Card:
    # 3.
    # everytime a card is rendererd it will be a Ace of hearts for now:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):      # if a class has this specific method, it's called upon when the print() method is used on an instance of this class
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    # 2. 

    def __init__(self):
        self.cards = []
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
                self.cards.append([suit, rank])

    def shuffle(self):
        # use the random library to shuffle the list of cards:
        if len(self.cards) > 1:     # If a deck doesn't contain more then 1 card it needs no shuffling
            random.shuffle(self.cards)


    def deal(self, number):
        """ Create an empty list and pop of the last item in cards. Append that item the empty list """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:     # Before dealing you'll want to check if the cards list is not empty.
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

# Create a new instance of the just created Card class:
card1 = Card("hearts", {"rank": "J", "value": 10})

print(card1)