from art import logo
print(logo)
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

num1 = float(input("Enter the first number \n"))
for i in operations:
  print(i)
operation = input("Enter the operation from the above you want to perform \n")

num2 = float(input("Enter the second number \n"))
calculation = operations[operation]
answer = calculation(num1,num2)
print(f"{num1} {operation} {num2} = {answer}")
status = input("Enter y to continue and n to stop \n")

while (status == "y"):
  num_1 = answer
  operation_loop = input("Enter the opeations from the above you want to perform \n")
  num_2 = float(input("What's the next number? \n"))
  calculation_loop = operations[operation_loop]
  answer= calculation_loop(num_1, num_2)
  print(f"{num_1} {operation_loop} {num_2} = {answer}")
  status = input("Enter y to continue and n to stop \n")
