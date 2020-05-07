#!/bin/python3

from random import randint
import os

os.system('cls')
print("\n\nWelcome to RPS Game using Python")
print("\nType(q) to QUIT?\nAnd here you go\n")
choice = ['r' ,'p' ,'s']

while True:
	user = input("\nChoose \nROCK(r), PAPER(p), SCISSOR(s) : ").lower()

	if user == 'q':
		exit()
	elif user not in choice:
	  print("Non of use")
	 
	else: 
		#initialize computer choice
		comput = randint(0,2)
		chosen = choice[comput]
		
		print(user," vs ",chosen)

		if chosen == user:
		  print("DRAW!!!")
		elif user == 'r' and chosen == 's':
		  print("You won")
		elif user == 'p' and chosen == 'r':
		  print("You won")
		elif user == 's' and chosen == 'p':
		  print("You won")
		elif user == 'r' and chosen == 'p':
		  print("Huh! you loss")
		elif user == 'p' and chosen == 's':
		  print("Huh! you loss")
		elif user == 's' and chosen == 'r':
		  print("Huh! you loss")  

