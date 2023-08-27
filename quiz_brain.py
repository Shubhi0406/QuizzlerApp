import html


# creates the QuizBrain class
class QuizBrain:
    # initializes an object with temporary values for four attributes
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # determines if any questions are left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # provides the next question in the list
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # returns it in the string format to be displayed to the user
        return f"Q.{self.question_number}: {q_text}"

    # checks the user's answer
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            # increments the score by 1 if the answer is correct and returns True
            self.score += 1
            return True
        else:
            # does not make any change if the answer is wrong and returns False
            return False

