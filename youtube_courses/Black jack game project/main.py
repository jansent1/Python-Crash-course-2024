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

# 1. 
suits = ["spades", "clubs", "heart", "diamonds"]
suit = suits[2]
rank = "K"
value = 10
print("Your card is: " + rank + " of " + suit)
# or: print(f"Your card is: {rank}")    to use something called an fString.
suits.append("snakes")
for suit in suits:
    print(suit)