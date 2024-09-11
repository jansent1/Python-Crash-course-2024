  # Dictionary: Key-value pairs, unordered and mutable.

# regular syntax:
mydict = {"name": "Max", "age": 28, "city": "New York"}
print("Using just curley braces: ", mydict)

# Using dict():
mydict2 = dict(name="Mary", age=27, city="Boston")
print("using the dict() function: ", mydict2)

# Accessing values in a dict:
value = mydict["name"]
print("Using the key to print the value: ", value)

# Add or change values after creation:
mydict["email"] = "max@google.com"
print("Adding an email adress: ", mydict)
mydict["name"] = "Tom"
print("Updated the name value: ", mydict)

# Delete items:
del mydict["name"]
print("Delete the name: ", mydict)
# pop an item:
value = mydict.pop("email")
print("Popped the last value pair: ", mydict)
# Pop the last added item:
value2 = mydict.popitem()
print("Pop the last added item: ", mydict, value2)

mydict = {"name": "Max", "age": 28, "city": "New York"}     # Fill the dict again with original records

# Check for a value:
if "name" in mydict:
    print("yes")
else:
    print("no")

# Or like this:
try:
    print(mydict["name"])
except:
    print("error")

# loop through a dictionary:
for key in mydict:
    print("Acces the key with a loop: ", key)

# Or acces both key and value:
for key, value in mydict.items():
    print("Loop through the complete record: ", key, value)

# Copy a dictionay:
mydict_cpy = mydict         # changes in the copy will also affect the original dict
mydict_cpy = mydict.copy()  # This will create an actual copy on its own memory space.
mydict_cpy = dict(mydict)   # This will create an actual copy on its own memory space.

# Merge two dictionairies with the update method:
my_dict = {"name": "Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict_2)
print("Existing pairs are overwritten and non existing are added: ", mydict)

# Keys can be numbers:
my_dict_3 = {3: 9, 6: 36, 9: 81}

