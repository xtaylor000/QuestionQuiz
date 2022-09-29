from question_model import Question
from data import question_data
from quizbrain import QuizBrain

from intro import intro

intro()
question_bank = []

for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
  quiz.next_question()

print(f"""
You've completed the quiz
Your final score is {quiz.score} / {len(question_bank)}
""")
