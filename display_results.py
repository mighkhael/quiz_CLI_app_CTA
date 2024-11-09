from questions import PASS_MARK 


#Display success or failure message based on the score.

def display_result(score):                      
    print("\n--- Quiz Complete ---")
    print(f"Your Score: {score:.2f}%")
    if score >= PASS_MARK:
        print("Congratulations, you passed!")
    else:
        print("Sorry, you failed. Better luck next time!")