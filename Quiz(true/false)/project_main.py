from project_14a import question_data
from project_14b import question
from project_14c import quizbrain

question_bank = []#array of objects
for question1 in question_data:
    question_text = question1["text"]
    question_answer = question1["answer"]
    new_question =question(question_text,question_answer)
    question_bank.append(new_question) 

quiz = quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"\nyour final score is --> {(quiz.score)}/{len(question_bank)}")