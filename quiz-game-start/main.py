from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_i = Question(text, answer)
    question_bank.append(question_i)


quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
    quizbrain.next_question()

print(f"You've completed the quiz, your final score is: {quizbrain.correct_answer_count} / {quizbrain.question_number}")
