import random
input("WELCOME TO THE GUSSEING GAME")
num=random.randint(1,100)

while True:
  num_enter=(input("Enter number between 1 to 100:"))
  num_enter=int(num_enter)
 
  if num_enter>num:
     print("You gussed too high")
  elif num_enter<num:
     print("You gussed too low")
  else:
     print("You gussed correct")
     break
