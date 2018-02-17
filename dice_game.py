#Dice Rolling Simulator

import random

def roll (sides = 12):
	num_rolled = random.randint(1, sides)
	return num_rolled

def main():
	sides = 12
	rolling = True
	print("Welcome to NerdyDevs Dice Roller!\n")
	while rolling:
		roll_again = input("Ready to Roll? ENTER=Roll Q=Quit")
		if roll_again.lower() != 'q':
			num_rolled = roll(sides)
			print("You rolled a", num_rolled)
		else:
			rolling = False
	print("Thanks for playing!")

main()				