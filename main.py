from dice_rolling import dice_rolling
from rock_paper_scissors import rock_paper_scissors
from tic_tac_toe import tic_tac_toe


while True:
    print("\n🎮 Python Games Menu")
    print("1. Dice Rolling 🎲")
    print("2. Rock Paper Scissors ✂️")
    print("3. Tic Tac Toe ❌⭕")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStarting Dice Rolling Game...\n")
        dice_rolling()

    elif choice == "2":
        print("\nStarting Rock Paper Scissors...\n")
        rock_paper_scissors()

    elif choice == "3":
        print("\nStarting Tic Tac Toe...\n")
        tic_tac_toe()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Please try again.")