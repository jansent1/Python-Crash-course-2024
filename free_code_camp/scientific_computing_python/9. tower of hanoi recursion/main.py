NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1

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

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True              
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods,'\n')


# Move Algorithm using ITTERATION:
def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target) 


# initiate call from source A to target C with auxiliary B:
move(NUMBER_OF_DISKS, 'A', 'B', 'C')