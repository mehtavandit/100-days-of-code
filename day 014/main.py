from game_data import data
from art import logo
from art import vs
import random

print(logo)
score = 0
play=True
while play:
  num1= random.randint(0,49)
  num2= random.randint(0,49)
  fol1= data[num1]['follower_count']
  fol2= data[num2]['follower_count']
  print(f"Comapre A: {data[num1]['name']}, {data[num1]['description']}, from {data[num1]['country']}")
  print(vs)
  print(f"Comapre B: {data[num2]['name']}, {data[num2]['description']}, from {data[num2]['country']}")
  choice = input("Who has more followers? Type 'A' or 'B':")
  if(fol1>fol2 and choice == "A"):
    score+=1
    print(f"You are right!!!, current score is {score}")
  elif(fol1<fol2 and choice == "B"):
    score+=1
    print(f"You are right!!!, current score is {score}")
  else:
    print("Sorry, your guess is wrong")
    print(f"final score is {score}")
    play = False
