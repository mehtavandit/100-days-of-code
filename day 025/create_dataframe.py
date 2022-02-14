import pandas

data_dict = {
    "students": ["Vandit","Mehta"],
    "scores" : [76,66]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")