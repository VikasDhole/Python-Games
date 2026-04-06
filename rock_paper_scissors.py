import random

def rock_paper_scissors():
    print("\n✂️ Rock Paper Scissors")
    print("=" * 30)

    choices = ["rock", "paper", "scissors"]

    while True:
        player = input("\nEnter rock/paper/scissors: ").lower()

        if player not in choices:
            print("❌ Invalid choice!")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("🤝 It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("✅ You win!")
        else:
            print("❌ You lose!")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break


# IMPORTANT FIX
if __name__ == "__main__":
    rock_paper_scissors()