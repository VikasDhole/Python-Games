import random

def number_guessing_game():
    print("\n🔢 Number Guessing Game")
    print("=" * 35)

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100")

    while True:
        guess = input("Enter your guess: ").strip()

        # Input validation
        if not guess.isdigit():
            print("❌ Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

    # Pause so user can see result
    input("\nPress Enter to return to menu...")


# IMPORTANT (prevents auto-run issue)
if __name__ == "__main__":
    number_guessing_game()