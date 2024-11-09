#importing modules

# import questions 

 # Calculate the percentage score based on correct answers.

def calculate_score(user_answers, correct_answers):
    correct_count = sum(1 for user_ans, correct_ans in zip(user_answers, correct_answers) if user_ans == correct_ans)
    return (correct_count / len(correct_answers)) * 100
