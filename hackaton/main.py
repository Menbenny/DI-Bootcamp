# quiz game which randomly prompts unversal questions, runs on terminal

from random import random 

user_inpput = input("")

def quiz_game():
    new_input = random(user_inpput)

import random

# List of questions
questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What is the currency of Japan?",
    "Who is the author of 'To Kill a Mockingbird'?",
    # Add more questions here
]

# List of corresponding answers
answers = [
    "Paris",
    "Leonardo da Vinci",
    "Jupiter",
    "Yen",
    "Harper Lee",
    # Add more answers here
]

def ask_question():
    # Randomly select a question
    index = random.randint(0, len(questions) - 1)
    question = questions[index]
    answer = answers[index]
    
    # Prompt the question to the user
    user_input = input(question + " ")
    
    # Check the answer
    if user_input.lower() == answer.lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", answer)

def main():
    print("Welcome to the Random Question Game!")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("Press Enter to get a random question: ")
        
        if user_input.lower() == "quit":
            break
        
        ask_question()
    
    print("Thanks for playing the game!")

if __name__ == '__main__':
    main()


