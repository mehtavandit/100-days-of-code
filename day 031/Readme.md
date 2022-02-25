<h1 align="center">
    100 Days of Code: Day 29
  <br>
</h1>

<h1 align="center">
    <a href="https://ibb.co/5184CkR"><img src="https://i.ibb.co/wdWg87z/Capture.png" alt="Capture" border="0"></a>
</h1>


## Objective
- This project's goal is to build a flash card game that kids can use to learn any new language.

## main.py
- A graphical user interface is constructed using tkinter, with a canvas size of 526 × 800 in which the words will be displayed. 
- When the user presses the play button, a window with a French term appears on the screen.
- The user will be given three seconds to estimate the answer, and the answer to that French term will be revealed on the screen in English language after three seconds.
- The user now has two options: a cross button if they don't know the answer and a checkmark button if they do.
- If the user presses the cross button, the next French term will appear on the screen and the three-second countdown will begin again.
- If the user clicks the checkmark button, the French term shown on the screen is removed from the dataset.
- When the game is finished, a new dataset titled "words to learn.csv" will be produced that contains the words that the user did not know.
