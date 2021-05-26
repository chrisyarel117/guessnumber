import random

firstname = input("Enter Your First Name: ")
lastname = input("Enter Your Last Name: ")
attempts = 0
number = random.randint(0,10)  ###this has the program choose a randome integer number between a & b.

print("Welcome to Guess the Secret Number Game.")
print("Start now!")

while (attempts < 7):
	guess = int(input("Enter the secret number: "))
	attempts += 1
	if (guess > number):
		print("Number is too high, it is less than 10.")
		print("Try Again!")
	elif (guess < number):
		print("Number is too low, number is more than 1.")
		print("Try Again!")
	elif (guess == number):
		print("You have won the Game!")
		break
if (attempts == 7):
    print("You have lost the game. The selected number is: ", number)
    
	
