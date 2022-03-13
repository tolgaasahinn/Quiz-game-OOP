from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

print(logo)
print("""
Please Choose Your Topic
1. Science
2. General Knowledge
3. History
""")
topic = input("Please Choose Your Topic:")
question_bank = []
topic = int(topic)
for i in range(len(question_data[topic])):
    question = Question(question_data[topic][i]["question"], question_data[topic][i]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_quesiton():
    quiz.next_question()
