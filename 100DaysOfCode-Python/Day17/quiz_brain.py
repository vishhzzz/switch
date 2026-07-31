class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question_text = self.question_list[self.question_no].text
        question_ans = self.question_list[self.question_no].ans
        # increase question no
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {question_text} (True/False)?: ")
        self.check_ans(user_ans, question_ans)

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_ans(self, user_ans, question_ans):
        if user_ans.lower() == question_ans.lower():
            self.score += 1
        else:
            print("Thats Wrong !!!")
        print(f"The correct ans is: {question_ans}")
        print(f"Your current score is: {self.score}/{self.question_no}\n")