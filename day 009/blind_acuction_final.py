from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bid_dict={}
print("Welcome to the auction:")
play = True
while play:
  name = input("What is your name?")
  amount = int(input("What's your bid?"))

  bid_dict[name] = amount
  
  status = input("Are there any other bid? Type 'yes' or 'no'")
  if(status == "yes"):
    play=True
    clear()
  else:
    play=False


max_bid = 0

for key in bid_dict:
  if(bid_dict[key] > max_bid):
    max_bid = bid_dict[key]

for key in bid_dict:
  if(bid_dict[key] == max_bid):
    print(f"The winner is {key}")

  
