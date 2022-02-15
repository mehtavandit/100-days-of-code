import pandas

data = pandas.read_csv("nato.csv")

alpha_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(alpha_dict)

user_text = input("Enter a word:- ").upper()
text_list = [alpha_dict[i] for i in user_text]
print(text_list)
