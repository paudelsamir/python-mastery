class QuizBrain:
    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
        self.current_score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        correct_answer = current_question.answer
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)
    
    def still_has_question(self):
        return self.question_no < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.current_score+= 1
            print(f"Your Current Score is: {self.current_score}/{self.question_no} ")
        else: 
            print("That's Wrong!")
            print("The correct answer was:", correct_answer)
            print(f"Your Current Score is: {self.current_score}/{self.question_no} ")