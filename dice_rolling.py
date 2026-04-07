import random

def dice_rolling():
    print("\n🎲 Dice Rolling Game")
    print("=" * 30)

    rounds_input = input("Enter number of rounds: ")

    if not rounds_input.isdigit():
        print("❌ Please enter a valid number!")
        return

    rounds = int(rounds_input)

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        print("🎲 Rolling...")

        player = random.randint(1, 6)
        computer = random.randint(1, 6)

        print(f"You rolled: {player}")
        print(f"Computer rolled: {computer}")

        if player > computer:
            print("✅ You win!")
        elif computer > player:
            print("❌ Computer wins!")
        else:
            print("🤝 Tie!")

    input("\nPress Enter to return to menu...")