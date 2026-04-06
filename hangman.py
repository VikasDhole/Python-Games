import random

def hangman():
    print("\n🎯 Hangman Game")
    print("=" * 30)

    words = ["python", "github", "developer", "computer"]
    word = random.choice(words)

    guessed = []
    attempts = 6

    while attempts > 0:
        display = [c if c in guessed else "_" for c in word]
        print("\nWord:", " ".join(display))
        print("Attempts left:", attempts)

        if "_" not in display:
            print("🎉 You won!")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("❌ Enter one letter only!")
            continue

        if guess in guessed:
            print("⚠️ Already guessed!")
            continue

        guessed.append(guess)

        if guess not in word:
            print("❌ Wrong!")
            attempts -= 1

    else:
        print(f"😢 You lost! Word was: {word}")

    input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    hangman()