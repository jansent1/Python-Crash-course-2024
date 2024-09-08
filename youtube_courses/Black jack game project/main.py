
# Note that now we've created a Card and Deck class that are usable for basicly any card game

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
    # everytime a card is rendererd:
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
                self.cards.append(Card(suit, rank)) # instead of appending suit and rank, we'll append an instance of the card class. Now it's filled with cards 

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

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer        # True if the instance is the dealer's hand.
    def add_card(self, cards_list):
        self.cards.extend(cards_list)
# Add the ability to calculate the value of a hand:
    def calculate_value(self):
        self.value = 0
        has_ace = False         # we don't need self because this variable is only used right here. 

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == 'A':        # check for an Ace which can be 1 OR 11
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    
    # Return True if blackjack occured:
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self):
        # 3 single quotes to be able to use single and double quotes inside your f string:
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')    # Ternary operator to check if self.dealer is True
        for card in self.cards:
            print(card)

        if not self.dealer:
            print("Value: ", self.get_value( ))
        print("")


# create a new deck instance and shuffle it:
deck = Deck()
deck.shuffle()

# create a new Hand instance and add 2 cards from the cards_dealt list:
hand = Hand()
hand.add_card(deck.deal(2))

# test case:
hand.display()