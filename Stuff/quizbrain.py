class QuizBrain:

  def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_list = q_list

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(
      f"\nQ.{self.question_number}: {current_question.text}?: "
    ).lower()

    self.checkanswer(user_answer, current_question.answer)

  def checkanswer(self, useranswer, correctanswer):

    if useranswer == correctanswer.lower():
      self.score += 1
      print("You got it right!")

    else:
      print("Nah thats wrong.")
    print(f"The correct answer was {correctanswer}")
    print(f"Your current score is {self.score}/{self.question_number}")