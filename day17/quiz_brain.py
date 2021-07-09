class QuizBrain():
    """Manage the question, recibe a list of question objects"""
    #atributes, acces them with self.
    question_number = 0
    score = 0
    
    #methods
    def __init__(self,question_bank):
        self.question_list = question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        data_return = False
        user_answer = ""

        while user_answer not in ['true','t','false','f']:
            user_answer = input (f"Q.{self.question_number}: {current_question.text}\nType True or False for your answer: ").lower()
            if user_answer not in ['true','t','false','f']:
                print("Wrong answer, please type a valid option\n")

        if user_answer in ['true','t']:
            user_answer = "True"
        else:
            user_answer = "False"
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}!")
        print(f"S C O R E = {self.score}/{self.question_number}\n")
     
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
