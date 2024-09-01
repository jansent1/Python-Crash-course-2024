NUMBER_OF_DISKS = 3
# A, B, C represent the rods and the lists with numbers represent the disks:
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)), # Generate a sequence of number counting down
    'B': [],
    'C': []
}

"""
The goal of the Tower of Hanoi is moving all the disks to the last rod. To do that, you must follow three simple rules:
You can move only top-most disks
You can move only one disk at a time
You cannot place larger disks on top of smaller ones

The Tower of Hanoi puzzle can be solved in 2**n - 1 moves, where n is the number of disks.
"""

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # move the nth disk from source to target
    target.append(source.pop())
        
    # display our progress
    print(A, B, C, '\n')
        
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)