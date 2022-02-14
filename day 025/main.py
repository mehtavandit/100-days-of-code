# with open("225 weather_data.csv") as file:
#     data_list = file.readlines()
#     print(data_list)

# import csv
# temp = []
# with open("225 weather_data.csv") as file:
#     data = csv.reader(file)
#     print(type(data))
#     for i in data:
#         #print(type(i[1]))
#         if i[1] != "temp":
#             temp.append(int(i[1]))
#
#
#     print(temp)

import pandas

data = pandas.read_csv("225 weather_data.csv")
#  print(data["temp"])

# Get data from particular column
data_dict = data.to_dict()
# print(data_dict)

#temp_list = data["temp"].to_list()
# sum = 0
# for i in temp_list:
#     sum+=i

#print(sum/len(temp_list))


print(data["temp"].mean())
print(data["temp"].max())


# Get data from particular row

