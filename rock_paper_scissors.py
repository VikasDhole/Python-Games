import random

def rock_paper_scissors():
    print("=" * 40)
    print("     Rock Paper Scissors Game!      ")
    print("=" * 40)

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        print("\n1. Rock 🪨  2. Paper 📄  3. Scissors ✂️")
        player = input("Your choice: ").lower()

        if player not in choices:
            print("⚠️ Invalid choice! Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("🤝 It's a Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("🎉 You Win!")
            player_score += 1
        else:
            print("😢 Computer Wins!")
            computer_score += 1

        print(f"Score → You: {player_score} | Computer: {computer_score}")

        again = input("\nPlay again? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for playing! 👋")
            break

rock_paper_scissors()