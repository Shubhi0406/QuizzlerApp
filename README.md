# THE QUIZZLER APP
#### Video Demo:  https://youtu.be/7Acvgda7JMM
#### Description:
THE QUIZZLER APP is a trivia game that poses random questions, taken from the website https://opentdb.com/api.php via its API. It has a simple interface, providing the user with 2 options: True or False to answer the question displayed.

The questions are from the category 'Computers' and each quiz has a total of 10 questions. The score is calculated as the user answers the questions and the updated score is displayed throughout the game.

The project folder has five files, each equipped to carry out a specific task. There is also an images folder that has icons of true and false to display to the user.

#### data.py
Using the requests module, questions are randomly picked from the trivia database using fixed parameters of number of questions, type, and category. The results are then returned by extracting them from the response in json format.

#### question_model.py
It creates the Question class and initializes the object, providing attributes of text and answer. 

#### quiz_brain.py
This file creates the QuizBrain class and initializes the object, providing attributes of question number, score, list of questions, and current question.
####
The still_has_questions function determines if there are still any questions remaining to ask from the list of questions. It does this by comparing the current question number with the length of the list of questions.
####
The next_question function returns the new question with the question number and text. First, it uses the question_number as the index for the list of questions and assigns the current question text to a variable. Then it updates the question number by incrementing it by 1. Finally, it ensures all symbols are displayed appropriately using the html module, and then it returns the required variables in the form of a string.
####
The check_answer function takes in the user's answer as an argument and determines whether the answer was right or not, and updates the score accordingly. First, it compares the user's answer with the answer attribute. If they are the same, it increments the score attribute by 1, and returns True. Otherwise, it returns False.

#### ui.py
Imports the tkinter module for providing a user interface. Sets the theme color as `#375362`.
####
Creates a QuizInterface class that initializes the object and configures the tkinter canvas. It populates the canvas with the question text, true and false buttons, and a score label.
####
The get_next_question function is used to update the canvas by displaying the current score and the text of the new question. The buttons are also made active to allow the user to provide an answer to the new question. However, if there are no more questions remaining (determined by the still_has_questions function of the QuizBrain class), it shows the final screen with updated text and the final score. The buttons are also disabled.
####
The true function is called when the user presses the 'True' button and the false function is called when the user presses the 'False' button. These functions first disable the buttons to prevent any other answers, and then check the answer. Finally, they call the give_feedback function to change the screen accordingly.
####
The give_feedback function takes the is_right variable as argument which tells whether the user's answer was correct or not. If it was right, the background is changed to green, and otherwise to red. It then waits 1 second to get the next question.
####
The buttons_state function is used to configure the state of the button as active or disabled.

#### main.py
Using the data in each file, it first loops through each question to create a Question object with text and answer, and then creates a question bank using the Question objects. Finally, it creates QuizBrain and QuizInterface objects to start the quiz.