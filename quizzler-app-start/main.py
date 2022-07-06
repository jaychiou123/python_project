from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

data_list = response.json()["results"]


question_bank = [Question(i["question"], i["correct_answer"]) for i in data_list]


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
