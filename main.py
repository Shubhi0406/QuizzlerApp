# imports classes from each file
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# creates a question bank using questions in the question list obtained from the trivia database
question_bank = []
for question in question_data:
    # assigns the question and answer to separate variables
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # creates a Question object using the two new variables
    new_question = Question(question_text, question_answer)
    # adds this new question to the question bank
    question_bank.append(new_question)

# creates an object of the QuizBrain class to make the quiz function
quiz = QuizBrain(question_bank)
# creates an object of the QuizInterface class to make the quiz interactive
quiz_ui = QuizInterface(quiz)
