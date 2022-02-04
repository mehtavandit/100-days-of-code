with open("./Input/Names/invited_names.txt") as name_file:
    names_list = name_file.readlines()
    print(names_list)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_data = letter_file.read()
    for i in names_list:
        i_strip = i.strip()
        new_invitaiton = letter_data.replace("[name]", i_strip)
        with open(f"./Output/ReadyToSend/letter_for_{i_strip}.txt", mode="w") as letter:
            letter.write(new_invitaiton)
