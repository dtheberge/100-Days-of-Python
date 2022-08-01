from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    temp = Question(item['text'], item['answer'])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while(quiz.stillHasQuestions()):
    quiz.nextQuestion()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.user_score}/{len(question_bank)}")