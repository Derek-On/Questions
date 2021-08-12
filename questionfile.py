#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

#chickens = 2 legs
#cows = 4 legs
#dogs = 4 legs

#The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a script or function that returns the total number of legs of all the animals.

#Example 1
#animals(2, 3, 5) ➞ 36

#Example 2
#input(1, 2, 3) ➞ 22

#Example 3
#How many Chickens? 5
#How many Cows? 2
#How many Dogs? 8
#50 legs

#Create a python script to solve this problem.

#Defined Leg counter function
def leg_counter():
	#define legs variable
	legs = 0
	#Create chickens, cows, and dogs variables using user input
	chickens = input("How many chickens? ")
	cows = input("How many cows? ")
	dogs = input("How many dogs? ")
	#Checks to make sure a integer is entered for each variable. raising an exception if the value of the variable is not a number.
	try:
		#Multiplies each variable by the number of legs that creature has, adding the result to the legs variable
		legs += 2*int(chickens)
		legs += 4*int(cows)
		legs += 4*int(dogs)
	except ValueError:
		#Tells the user that their input is invalid, and what a valid input looks like
		print("Only numbers are valid, and a number must be entered for each animal")
	#Returns a string containing the number of legs.			
	return "{} legs".format(legs)

#Runs the leg_counter function, printing the returned variable.
print(leg_counter())



