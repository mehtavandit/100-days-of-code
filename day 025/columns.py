import pandas

data = pandas.read_csv("225 weather_data.csv")

print(data["temp"])    # Treating the dataset as dictionary, and pulling out each column as a key
print(data.temp)       # Treating the dataset as object, and pulling out each column as a attribute