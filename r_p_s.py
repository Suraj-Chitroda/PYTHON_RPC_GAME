#!/bin/python3

from random import randint

user = input("Choose \n ROCK(r), PAPER(p), SCISSOR(s) : ")

choice = ['r' ,'p' ,'s']
if user not in choice:
  print("Non of use")
  exit()

#initialize computer choice
comput = randint(1,3)
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






