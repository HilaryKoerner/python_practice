#create a variable list and set is as a list
my_list = ["Jacob", 25, "Ahmed", 80]
print(my_list)

#append an element to the list (.append is a method of my_list)
my_list.append("Matt")
print(my_list)

#return the index of the first object with the matching value (.index is a method of my_list)
print(my_list.index("Matt"))

#change a specified element (could be any element) at the given index (in this case, we are changing the 3rd index)
# = is assignment in this case
my_list[3] = 85
print(my_list)

# return the length of the list
print(f"There are {len(my_list)} objects in the list" )

# remove an object from the list
my_list.remove("Matt")
print(my_list)

# .pop method removes an object at the index specified

my_list.pop(0)
print(my_list)

# creates a tuple. A tuple is a sequence of immutable python objects that cannot be changed

my_tuple = ("Python", 100, "VBA", False)
print(my_tuple)


