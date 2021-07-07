#initial variable to start the while loop
user_play = "y"

while user_play == "y":
    user_number = int(input("Enter a number"))

    #added in the 1 and +1 to account for range (which goes from 0 up until the user number)
    for x in range(1, user_number + 1):
        print (x)
    
    #print question to continue or kill the loop
    user_play = input("continue: (y)es or (n)no?")