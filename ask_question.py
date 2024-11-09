
#importing the questions' module

import questions 


    #Display the question and choices, and get the user's answer.

def ask_question(question, choices):                   #Display the questions and choices and get user's answer
	print(f"\n{questions}")
	for choice in choices:
		print(choice)
	answer = input("your answer (A/B/C/D):  ").strip().upper()
	return answer 


# Sample question and choices

# question = "What is the capital of France?"
# choices = ["A) Berlin", "B) London", "C) Paris", "D) Rome"]

# # Call the function with the sample question and choices

# user_answer = ask_question(question, choices)
# print(f"You selected: {user_answer}")
