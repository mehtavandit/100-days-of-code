<h1 align="center">
    100 Days of Code: Day 17
  <br>
</h1>

## Objective
- This project's purpose is to construct a True or False quiz game with ten questions.

## main.py
- The ten questions are saved in a list named question_bank.
- Using a while loop, each question is asked one at a time, and a score is shown on the screen once each question is answered.
- The final score is revealed at the completion of the quiz.

## quiz_brain.py
- Initial question number and score are both set to zero.
- A function still_has_questions() checks whether there is any other questions left or not.
- A function next_question() selects the question and displays it on the screen.
- When the user inputs the response, the function check_answer() evaluates whether or not the answer is correct.
- If the answer is correct, the score is increased by one and the message "You got it right!" appears on the screen.
- If the response is incorrect, the message "That wrong." is shown on the screen.
-
## data.py
- This file contains all the 10 questions and answers.

## question_model.py
- Extract the question text and answer from the question_bank list.
