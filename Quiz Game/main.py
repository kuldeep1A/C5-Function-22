from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# print(QuizBrain(question_bank))
while quiz.still_has_question():  # If quiz still has question remaining:
    quiz.next_question()

# t f t t t f t f t t f t
print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
