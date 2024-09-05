import random

flag = True
while flag:
    num = input("Type a number for an upper bound: ")

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print("Invalid input, try again!")

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    pass