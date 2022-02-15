import pandas

with open("file1.txt") as file:
  data = file.readlines()
  first_list = [int(n) for n in data]
  #print(first_list)

with open("file2.txt") as file:
  data = file.readlines()
  second_list = [int(n) for n in data]
  #print(second_list)

final_list = []

for i in first_list:
  for j in second_list:
    if(i==j):
      if i not in final_list:
        final_list.append(i)

print(final_list)
