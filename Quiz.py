import random

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("Enter '0' to exit the quiz.")
    user_answer = input("Enter the number of your answer: ")
    return user_answer

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        user_answer = display_question(question, options)

        if user_answer == '0':
            print("Exiting the quiz. Thank you for playing!")
            return

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}. \n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    print("Thank you for playing!")


def main():
    print("Welcome to the Quiz Application!")
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! Let's get started with the quiz.\n")

    # Quiz questions
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Paris", "Rome", "Madrid"],
            "correct_answer": 2,
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Mercury"],
            "correct_answer": 1,
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct_answer": 2,
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_answer": 1,
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1920", "1935", "1943"],
            "correct_answer": 1,
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
            "correct_answer": 3,
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Osmium", "Oganesson", "Orogonium"],
            "correct_answer": 1,
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            "correct_answer": 2,
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "correct_answer": 3,
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["Java", "Python", "JavaScript", "C++"],
            "correct_answer": 3,
        },
        {
            "question": "What is the currency of China?",
            "options": ["Yuan", "Won", "Ruble", "Ringgit"],
            "correct_answer": 1,
        },
        {
            "question": "Who is the author of 'To Kill a Mockingbird'?",
            "options": ["J.K. Rowling", "Harper Lee", "George Orwell", "Ernest Hemingway"],
            "correct_answer": 2,
        },
        {
            "question": "Which continent is known as the 'Land of Fire and Ice'?",
            "options": ["Africa", "Europe", "North America", "Antarctica"],
            "correct_answer": 4,
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Avocado", "Tomato", "Onion", "Lemon"],
            "correct_answer": 1,
        },
        {
            "question": "Who invented the telephone?",
            "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
            "correct_answer": 2,
        },
        {
            "question": "Which Shakespearean play features the character Macbeth?",
            "options": ["Romeo and Juliet", "Hamlet", "Othello", "Macbeth"],
            "correct_answer": 4,
        },
        {
            "question": "What is the capital of Brazil?",
            "options": ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"],
            "correct_answer": 3,
        }
    ]

    # Run the quiz
    run_quiz(quiz_questions)


if __name__ == "__main__":
    main()
