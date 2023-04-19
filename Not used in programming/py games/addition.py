import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return (num1, num2, num1 + num2)

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter your answer: "))
            return answer
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    score = 0
    num_questions = 5
    
    for i in range(num_questions):
        num1, num2, correct_answer = generate_question()
        print(f"Question {i+1}: What is {num1} + {num2}?")
        user_answer = get_user_answer()
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"Final score: {score}/{num_questions}")
    if score == num_questions:
        print("Congratulations, you got them all right!")
    else:
        print("Better luck next time!")
    
if __name__ == '__main__':
    main()
