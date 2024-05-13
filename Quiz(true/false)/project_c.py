class quizbrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if(self.question_number<len(self.question_list)):
            return True
        else:
            return False
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer=(input(f"\nQ.{(self.question_number)}: {current_question.text} (True/False)?:").lower())
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer, correct_answer):
        if(user_answer.lower() == correct_answer.lower()):
            print("you got it right")
            self.score+=1
            print(f"current score is --> {self.score}/{self.question_number}")
        else:
            print("you got it wrong")
            print(f"current score is --> {self.score}/{self.question_number}")
        print(f"the correct answer was {correct_answer}")