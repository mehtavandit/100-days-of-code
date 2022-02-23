import pandas

data = pandas.read_csv("nato.csv")

alpha_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(alpha_dict)
go_on = True

while go_on:
    user_text = input("Enter a word:- ").upper()
    try:
        text_list = [alpha_dict[i] for i in user_text]
        print(text_list)
        go_on = False
    except KeyError:
        print("Only letters from dictionay are allowed")
