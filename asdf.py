

num1 = -1000
num2 = -900
#using a while loop with boolean and try/exceot


print(num1, num2)




#using a loop to go through a list
#myList = ["asdf", "qwer", "ghjk", "zxcv"]
#for i in myList:
#    print(i)




#make the multiplication table results up to THRESHOLD
#THRESHOLD = 5





##num = int(input("Enter a positive integer:"))
##while num >= 1:
## digit = num % 2
## num = num//2
## print(digit)





# Make a list of: 9, 18, 135
# One by one, add these elements to the list:  59, 123
# Add a new number, 93, into the second-last list slot by making reference to the list's length
# Change the last element's value to 1
# Use a for loop to display the list one element at a time

# 9-blastoise, 18-pidgeot, 135-jolteon, 59-arcanine
##battleTeam = [9, 18, 135, 59]
###print(battleTeam)
##
### 123-scyther
##battleTeam.append(123)
###print(battleTeam)
##
### 93-haunter
##battleTeam.insert(len(battleTeam)-1, 93)
###print(battleTeam)
##
### replace 123-scyther with 1-bulbasaur
##battleTeam[-1] = 1
##
##for p in battleTeam:
##    print(p)





#0- find the location of the value 13
#1- take out the first occurrence of 4 (don't specify an index)
#2- add the value 75 to the 4th slot of the list
#3- order the list
#4- flip the order of the list
##nice = [4, 7, 13, 99, 3, 4]
##print("OG list:", nice)
##
##print("Index is:", nice.index(13))
##nice.remove(4)
##print("Change 1)", nice)
##nice.insert(3, 75)
##print("Change 2)", nice)
##nice.sort()
##print("Change 3)", nice)
##nice.reverse()
##print("Change 4)", nice)


# Make a list of the following: 7, cookie, -1.79, False
# Access the list to show "cookie" in the display window.
# Then, use a for loop to print all list elements.

##newList = [7, "cookie", -1.79, False]
##print(newList[1])
##for i in newList:
##    print(i)



##def function1(something):
##    print("Hello")
##    function2("Watermelon")
##    return something
##
##def function2(somethingElse):
##    print(somethingElse)
##
### Main
##
##value = function1(2)
##print(value)





# Custom function: Takes 2 arguments user's name and their age.
# The function will add "Old" to the start of their name.
# It will also multiply their age with a random integer (from 1-5).
# Return both of the results to the main program.

# Tell the user (by name) this is their projected lifespan.
# Call the function and save their new name and age.
# Tell the user their "old" version of name and age.
# You do not need to comment, error check,
# or get user input (hard-coded values are fine).

##import random
##
##def lifespan(name, age):
##    oldName = "Old " + name
##    finalAge = age * random.randint(1,5)
##    return oldName, finalAge
##
##name, age = lifespan("Ryan", 18)
##print(str(name) + ", your projected lifespan is " + str(age) + " years.")




##def get_names():
##    first = input("Enter first: ")
##    last = input("Enter last: ")
##    return first, last
##
##name1, name2 = get_names()
##print(name1, name2)




##t1 = (-v - math.sqrt(v**2-4*-4.9*h)) / 2*-4.9
##t2 = (-v + math.sqrt(v**2-4*-4.9*h)) / 2*-4.9



#create a function that prints a random integer from 1 to 12 (inclusive)
#call that function

##import random
##
##def callMeMaybe():
##    heresMyNumber = random.randint(1,12)
##    print(heresMyNumber)
##
##callMeMaybe()

#purple = random.choice(["are", "we", "thurr", "yit"])
#print(purple)






##def friendship(name1, name2):
##    print(name1, "befriends", name2)
##
##friendship("Scorpion", "Sub-zero")



#keep asking user for numbers, exit when they enter the number 3
#inlcude error handling

#    num = int(input("enter a number; 3 exits: "))



##number = int(input("Enter a number: "))
##
##for i in range (1, number+1):
##    for j in range (1, number+1):
##        print("(" + str(i) + "," + str(j) + ")", end="")
##
##    print("\n")


##NumberOfRows = int(input("How many rows? "))
##
##for i in range (1, NumberOfRows +1):
##   # print("Row number: " + str(i) + "\n")
##    print("\n")
##
##    for j in range (1, i+1):
##        print("*", end="")
##    


#num = 2/7
#print("Quotient: {:.2f}".format(num))



#keep asking user for numbers, exit when they enter 3
#inlcude error handling
##num = -1
##while num != 3:
##    try:
##        num = int(input("enter a number; 3 exits: "))
##    except:
##        print("Incorrect number")
