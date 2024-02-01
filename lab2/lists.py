#exersize 1 
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#exersize 2 
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

#exersize 3 
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#exersize 4 
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

#exersize 5 
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

#exersize 6 
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#exersize 7 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#exersize 8 
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Example
mylist = ["apple", "banana", "cherry"]

#Example
#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Example
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Example
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Example
#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#Example
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Example
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Example
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Example
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Example
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Example
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Example
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Example
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Example
#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Example
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Example
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Example
#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Example
#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Example
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Example
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Example
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Example
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Example
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Example
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Example
#Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Example
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Example
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Example
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Example
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Example
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Example
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Example
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#Example
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Example
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Example 
#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

#Example
#With no if statement:
newlist = [x for x in fruits]

#Example
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

#Example
#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

#Example
#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#Example
#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

#Example
#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

#Example
#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example
#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Example
#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example
#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Example
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Example
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Example
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Example
#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Example
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Example
"""Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """






