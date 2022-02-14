import pandas

data = pandas.read_csv("225 weather_data.csv")

# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])

#print(data[data.temp == data["temp"].max()])

wed = data[data.day == "Wednesday"]
print(int(wed.temp)*1.8+32)
