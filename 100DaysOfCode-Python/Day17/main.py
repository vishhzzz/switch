# get data from data.py to here, the only diff here is:
# instead of list of dictionaries, we should have list of question objects

import data
from question_model import Question
from quiz_brain import QuizBrain

# list
question_list = []
for ele in data.question_data:
    question = Question(ele["text"], ele["answer"])
    question_list.append(question)

quiz = QuizBrain(question_list)

while quiz.still_has_question():
    # if there r questions remaining, keep asking next question
    quiz.next_question()

print("Quiz ended !!!")