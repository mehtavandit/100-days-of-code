import random
from replit import clear
from art import logo

print(logo)
def deal_card():
  """Selects a random card from the list"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  sel_card = random.choice(cards)
  return sel_card

def calculate_score(cards):
  """Calculates the sum of the list"""
  Sum = sum(cards)
  if(Sum == 21 and len(cards) == 2) :
    return 0

  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
    Sum = sum(cards)
    return Sum
  
  return Sum


def compare(user,comp):
  """Decides who is the winner"""
  if(user == comp):
    print("Game drawn")
  elif(comp == 0 and user!=0):
    print("You loose")
  elif(user == 0 and comp!=0):
    print("You won")
  elif(user>21):
    print("You loose because you went over")
  elif(comp>21):
    print("You won because computer went over")
  elif(user>comp):
    print("You win")
  else:
    print("You loose")
  

status = input("Type 'y' to play and 'n' to not play ")
while status == "y":
  user_cards = []
  computer_cards = []
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  user_score = calculate_score(user_cards)
  comp_score = calculate_score(computer_cards)

  print(f"Your cards:{user_cards}, Current score:{user_score}")
  print(f"Computers first card:{computer_cards[0]}")

  # if(user_score>21):
  #   print("You loose because you went over")
  #   break
  # if(comp_score>21):
  #   print("You won because computer went over")
  #   break

  decision = input("Type 'y' to get another card and type 'n' to stop: ") #both working
  while decision == "y":
    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    # if(user_score>21):
    #   print("You loose because you went over")
    #   status = "n"
    #   break
    print(f"Your cards:{user_cards}, Current score:{user_score}")
    print(f"Computers first card:{computer_cards[0]}")
    decision = input("Type 'y' to get another card and type 'n' to stop:")


  while comp_score<17:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)


  #comp_score = calculate_score(computer_cards)

  print(f"Your final hand is {user_cards}, final score: {user_score}")
  print(f"Computer's final hand is {computer_cards}, final score: {comp_score}")
  compare(user_score, comp_score)

  status = input("Type 'y' to play and 'n' to not play ")
  if(status == "y"):
    clear()
