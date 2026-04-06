import random

def dice_rolling():
    print("=" * 40)
    print("        Dice Rolling Game!          ")
    print("=" * 40)

    player_score = 0
    computer_score = 0
    rounds = int(input("How many rounds do you want to play? "))

    for round in range(1, rounds + 1):
        print(f"\n--- Round {round}/{rounds} ---")
        input("Press Enter to roll your dice... 🎲")

        player_dice = random.randint(1, 6)
        computer_dice = random.randint(1, 6)

        print(f"You rolled:      {player_dice} 🎲")
        print(f"Computer rolled: {computer_dice} 🎲")

        if player_dice > computer_dice:
            print("✅ You win this round!")
            player_score += 1
        elif computer_dice > player_dice:
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a Tie!")

    print("\n" + "=" * 40)
    print(f"Final Score → You: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("🏆 You are the Winner!")
    elif computer_score > player_score:
        print("😢 Computer Wins Overall!")
    else:
        print("🤝 Overall it's a Draw!")
    print("=" * 40)

    again = input("\nPlay again? (yes/no): ")
    if again.lower() == "yes":
        dice_rolling()
    else:
        print("Thanks for playing! 👋")

dice_rolling()