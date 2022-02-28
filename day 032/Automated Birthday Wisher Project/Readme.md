## Objective
- This project's purpose is to develop an automated birthday wisher.

## main.py
- When the user selects the run button, all of the data in the "birthdays.csv" file is saved as a dictionary.
- The current month and data are stored in a tuple, and the dictionary created in step 1 is iterated.
- If a person's birthday month and date in the dictionary match the current month and date, an email greeting Happy birthday is sent to the relevant email id using smtplib library.
- This program can be automated by using the free version of **pythonanywhere**
