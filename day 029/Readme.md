<h1 align="center">
    100 Days of Code: Day 29
  <br>
</h1>

<h1 align="center">
  <a href="https://imgur.com/o5LcQK5"><img src="https://i.imgur.com/o5LcQK5.png" title="source: imgur.com" /></a>

## Objective
- This project's goal is to create a password management app.

- When you click the add button, all of the information is saved in the data.txt file.

## main.py
- A graphical user interface of the minimum possible size is constructed, with a canvas size of 200 × 200 in which a logo is inserted.
- There are three types of tkinter widgets used: - Label, Entry, and Button
- In this app, the user must input the name of the website as well as their email address.
- For the password, the user may either type it in or select the generate password option.
- When an user clicks the Generate Password Button, a function named create password() is invoked.
- This function generates a password of any length, which is automatically entered in the text box to the left of the Generate Password Button.
- When the user presses the Add Button, it is evaluated whether or not all of the Entry widgets have input. 
- If any of the Entry widgets are left blank, a pop-up window opens with the message "Please fill in all the blanks."
- When the user submits all of the data and clicks the Add Button, a pop-up window appears with the information provided by the user.
- If the user hits "ok," the information is saved in the text file; if the user clicks "cancel," the pop-up disappears and the user is given the opportunity to amend.

## data.txt
- This file includes the website's name, email address, and the user's password.

## logo.png
-  This file contains the logo.
