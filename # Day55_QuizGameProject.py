def run_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        choice = input("Your answer: ").upper()

        if choice not in ["A", "B", "C", "D"]:
            print("Invalid choice, please enter A, B, C, or D.")
            continue

        if choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nFinal Score: {score}/{len(questions)}")

while True:
    run_quiz()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break

{
    "question": "Which language is used for web development?",
    "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
    "answer": "B"
}

questions = [
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    print("🎯 Welcome to the Day 55 Quiz Game!")
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        choice = input("Your answer: ").upper()

        if choice not in ["A", "B", "C", "D"]:
            print("Invalid choice, please enter A, B, C, or D.")
            continue

        if choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

        print(f"Current Score: {score}")

    print(f"\nFinal Score: {score}/{len(questions)}")

while True:
    run_quiz()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break

