student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for key in student_scores:
  x = student_scores[key]
  if x>90:
    student_grades[key]="Outstanding"

  elif x>80:
    student_grades[key]="Exceeds Expectations"

  elif x>70:
    student_grades[key]="Acceptable"

  else:
    student_grades[key]="Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)





