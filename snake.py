#program to pay the snake and ladder game 
count=0
import random
while(count<=100):
	n=input("enter r to roll")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position",count)
		print("ur r value",a)

		if(count==8):
			count=37
			print("cong u hv climbed the ladder")
		elif(count==11):
			count=2
			print("sorry snake has bit")
		elif(count==13):
			count=34
			print("cong u hv climbed the ladder")
		elif(count==38):
			count=9
			print("sorry snake has bit")
		elif(count==40):
			count=68
			print("cong u hv climbed the ladder")
		elif(count==52):
			count=81
			print("cong u hv climbed the ladder")
		elif(count==65):
			count=46
			print("sorry snake has bit")
		elif(count==76):
			count=97
			print("cong u hv climbed the ladder")
		elif(count==89):
			count=70
			print("sorry snake has bit")
		elif(count==93):
			count=64
			print("sorry snake has bit")
		elif(count==100):
			count=100
			print(" you have won the game")
		elif(count>100):
			count=count-a
			print("u cant go beyound 100")
