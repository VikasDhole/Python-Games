import random

def dice_rolling():
    print("\n🎲 Dice Rolling Game")
    print("=" * 30)

    try:
        rounds = int(input("How many rounds do you want to play? "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    player_score = 0
    computer_score = 0

    for i in range(1, rounds + 1):
        input("\nPress Enter to roll dice...")

        player = random.randint(1, 6)
        computer = random.randint(1, 6)

        print(f"You rolled: {player}")
        print(f"Computer rolled: {computer}")

        if player > computer:
            print("✅ You win this round!")
            player_score += 1
        elif computer > player:
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

    print("\nFinal Score:")
    print(f"You: {player_score} | Computer: {computer_score}")


# IMPORTANT FIX
if __name__ == "__main__":
    dice_rolling()