"""
copper = {
    'species': 'Guinea Pig',
    'age': 2      
          }

print(copper['species'])

# add a new key/value pair:
copper['food'] = 'hay'
print(copper)

# reassign a value:
copper['species'] = 'Cavia porcellus'
print(copper)

# itterate over the KEYS in a dict:
for i in copper:
    print(i)

# itterate over the VALUES in a dict:
for i in copper.values():
    print(i)

# itterate over the KEYS/VALUE PAIRS in a dict (stored in tuples):
for i in copper.items():
    print(i)

# And to print the key value pairs as strings:
for i, j in copper.items():
    print(i, j)

# Remove a key/value pair:
del copper['age']

"""

# A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.
my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path():
    pass