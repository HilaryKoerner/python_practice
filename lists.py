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

