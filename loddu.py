#program to roll and quit the dice
import random
while True:
	i=input("enter r to roll or q to quit:")
	if (i=='r'):
		print(random.randint(1,20))
		exit()
	else:
		print("try again")