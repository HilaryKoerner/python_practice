#conditionals
## = assignment, == equality

x = 1
y = 10

if x == 1:
    print("x is equal to 1")

if y != 1:
    print("y is not equal to 1")

if x < y:
    print("x is less than y")

if y>x:
    print("y is greater than x")

if x == 1 and y == 10:
    print("x is 1 and y is 10") 

if x < 10:
    if y <5:
        print("x is less than 10, y is less than 5")
    elif y == 5:
        print ("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

