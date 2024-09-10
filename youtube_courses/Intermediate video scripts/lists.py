# Lists: ordered, mutable, allows duplicate items
myList = ["banana", "cherry", "apple"]      # Create a list
myList2 = list()    # Create an empty list or conver the parameter to a list.
myList2 = [1, 2, True, "pineapple", 3.14]       # fill the created list
print("myList: ", myList)
print("myList2: ", myList2)

# Check if an item is in a list:
if "banana" in myList:
    print("Yes, the item/index is found")
else:
    print("No, index/item not found")

print("The length of myList is: ",len(myList))      # check number of items in a list. (length)

myList.append("lemon")      # add lemon to myList
print("Lemon is added: ", myList)

# add blueberry at a specific index:
myList.insert(1, "blueberry")
print("BLeuberry added at index 1: ", myList)

# remove last item of the list:
item= myList.pop()
print("Last item pop(): ", item)
# remove specific item of the list:
myList.remove("cherry")
print("Remove cherry: ",myList)


# reverse a list:
myList.reverse()
print("Reversed list: ", myList)
# sort a list:
myList.sort()
print("Sort() changes/sorts the original list: ", myList)
# Don't alter the original:
myList3 = [42, 905, 5, 2, 23, 1]
new_list = sorted(myList3)
print("New_list: ", new_list, "original: ", myList3)

# create a new list with 5 duplicates:
myList4 = [0] * 5
print("5 duplicates: ", myList4)

# combine two lists:
myList5 = [1, 2, 3, 4, 5]
combined_list = myList4 + myList5
print("Combined lists: ", combined_list)

# clear all items:
# cleared_list = myList.clear()
# print("Cleared list: ", myList)

# slicing lists:
a = myList3[1:5]
print("Sliced myList3: ", a)  
b = myList3[:5]
print("Sliced myList3: ", b)
c = myList3[1:]
print("Sliced myList3: ", c)
d = myList[::2]
print("My list sliced with step 2: ", d)

# copying lists:
list_org = ["banana", "cherry", "apple"]
list_copy = list_org        # modify the copy will ALSO modify the original!!!

list_copy = list_org.copy() # modify the copy WILL NOT modify the original
list_copy = list(list_org)  # modify the copy WILL NOT modify the original
list_copy = list_org[:]     # slicing from beginning to end will make a copy.

# List comprehension: (fast way to create a new list from an original list)
myList7 = [1, 2, 3, 4, 5, 6]
b = [i*i for i in myList]       # expression and then a for loop 
print("Squared items in new list with comprehension: ", b)

 