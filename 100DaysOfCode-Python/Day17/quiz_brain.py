class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list

    def next_question(self):
        question_text = self.question_list[self.question_no].text
        question_ans = self.question_list[self.question_no].ans
        # increase question no
        self.question_no += 1
        ques = input(f"Q.{self.question_no}: {question_text} (True/False)?: ")