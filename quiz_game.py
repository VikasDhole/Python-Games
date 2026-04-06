def quiz_game():
    print("\n⏱️ Quiz Game")
    print("=" * 30)

    questions = {
        "What is the capital of India?": "delhi",
        "What is 5 + 5?": "10",
        "Python is a (language/tool)?": "language"
    }

    score = 0

    for q, ans in questions.items():
        user = input(q + " ").lower()

        if user == ans:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Answer: {ans}")

    print(f"\nYour score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()