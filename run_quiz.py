#importing modules

from questions import questions
from ask_question import ask_question
from calculate_scores import calculate_score
from display_results import display_result

   # Run the quiz application.

def run_quiz():
    user_answers = []
    correct_answers = []

    for question, (choices, correct_answer) in questions.items():
        answer = ask_question(question, choices)
        user_answers.append(answer)
        correct_answers.append(correct_answer)

    score = calculate_score(user_answers, correct_answers)
    display_result(score)


