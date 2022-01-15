# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = (weight)/height**2

if (BMI<18.5):
  print("Underweight")
elif (BMI<25):
  print("Normal Weight")
elif (BMI<30):
  print("Slightly Owerweight")
elif (BMI<35):
  print("Obese")
else:
  print("Clinically obese")


