from dice_rolling import dice_rolling
from rock_paper_scissors import rock_paper_scissors
from tic_tac_toe import tic_tac_toe
from number_guessing_game import number_guessing_game
from word_guessing import word_guessing
from calculator import calculator
from password_generator import password_generator
from quiz_game import quiz_game
from hangman import hangman


def main():
    while True:
        print("\n🎮 Python Games Hub")
        print("1. Dice")
        print("2. Rock Paper Scissors")
        print("3. Tic Tac Toe")
        print("4. Number Guessing")
        print("5. Word Guessing")
        print("6. Calculator")
        print("7. Password Generator")
        print("8. Quiz Game")
        print("9. Hangman")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            dice_rolling()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            number_guessing_game()
        elif choice == "5":
            word_guessing()
        elif choice == "6":
            calculator()
        elif choice == "7":
            password_generator()
        elif choice == "8":
            quiz_game()
        elif choice == "9":
            hangman()
        elif choice == "10":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()