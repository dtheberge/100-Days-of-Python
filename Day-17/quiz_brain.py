
class QuizBrain:
    def __init__(self, list) -> None:
        self.question_number = 0
        self.user_score = 0
        self.question_list = list

    def nextQuestion(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        
        user_answer = input(f"\nQ.{self.question_number + 1}: {question_text} (True/False)?: ")
        self.checkAnswer(user_answer, question_answer)
        self.question_number += 1

    def stillHasQuestions(self):
        if (self.question_number < len(self.question_list)):
            return True
        else:
            return False
        
    def checkAnswer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong..")
        print(f"The answer was {answer}.")
        print(f"Your current score is {self.user_score}.")
        