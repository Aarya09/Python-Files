import random
while True:
	d={1:'r',2:'p',3:'s'}
	c=d[random.randint(1,3)]
	u=input("enter'r','p','s'")
	print("computer chose",c)
	if(c==u):
		print("tie")
	elif((c=='r' and u=='s') or (c=='p' and u=='r') or (c=='s' and u=='p')):
		print("comp won the game")
	else:
		print("you won the game")
		 