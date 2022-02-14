import pandas

data = pandas.read_csv("squirrel data.csv")
data_list = data["Primary Fur Color"].to_list()
# print(data_list)

gray = 0
cinnamon = 0
black = 0

for i in data_list:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1
    else:
        pass

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

count = pandas.DataFrame(data_dict)
count.to_csv("squirrel_count.csv")
