import random
from art import logo
def play(guess,trials, number):
  if(guess>number):
    print("Too high")
    return trials-1
  elif(guess<number):
    print("Too Low")
    return trials-1
  else:
    print("That's a perfect guess")
    return
  
print(logo)
print("Welcome to the number guessing game")
print("I am thinking of the number between 1 to 100")
result = random.randint(1,100)
mode = input("Choose the difficulty, easy of hard:")
if(mode == "easy"):
  trials = 10
if(mode == "hard"):
  trials = 5
guess=0
while guess!=result:
  print(f"You have {trials} to guess the answer")
  guess = int(input("Make a guess: "))
  trials = play(guess, trials, result)
  if(trials == 0):
    print("You are out of attempts")
    print(f"The correct answer was {result}")
    break

