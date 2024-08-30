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