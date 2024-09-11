# Tuples: ordered, immutable and allow duplicate elements


# Create a tuple:
myTuple = ("Max", 28, "Boston")
print(myTuple)
# OR like this:
myTuple = tuple(["Max", 28, "Boston"])

# acces and index:
item = myTuple[1]
print("Print a single index: ", item)

# itterate over tuple:
for i in myTuple:
    print(i)

# check for item:
if "Max" in myTuple:
    print("Yes")
else:
    print("No")

# Length of a tuple:
print("Length of myTuple: ", len(myTuple))

# Count number of times an element is in de tuple:
print("Number of times 'Max'", myTuple.count("Mx"))

# find an index of an element:
print("Index: ", myTuple.index(28))

# slicing works the same as with the list slicing.

# unpacking a tuple:
my_tuple = "Max", 28, "Boston"      # You don't need the () notation in python for tuples
name, age, city = my_tuple          # this is called unpacking. The number of elements must equal the number of elements in the tuple!!!!
print(name, age, city)

# We can unpack multiple elements with a star:
my_tuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple
print(i1) # print the first item
print(i2) # Print everything in between in a list
print(i3) # print the last item.

#compare a tuple and a list:
"""
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

Working wit tuples can be more efficient that working with lists. Tuples are smaller.
Even when they contain the same elements. When working with large amounts of data this will
really influence your loading times.
"""