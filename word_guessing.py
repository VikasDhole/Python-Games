import random

def word_guessing():
    print("\n📝 Word Guessing Game")
    print("=" * 30)

    words = ["python", "github", "developer", "keyboard"]
    word = random.choice(words)

    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("\nWord:", " ".join(display))
        print("Attempts left:", attempts)

        if "_" not in display:
            print("🎉 You guessed the word!")
            break

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter a single valid letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("❌ Wrong guess!")
            attempts -= 1

    else:
        print(f"😢 Game Over! Word was: {word}")

    input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    word_guessing()