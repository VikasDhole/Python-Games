def tic_tac_toe():
    print("=" * 40)
    print("         Tic Tac Toe Game!          ")
    print("=" * 40)

    board = [" " for _ in range(9)]

    def print_board():
        print(f"\n {board[0]} | {board[1]} | {board[2]}")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]}\n")

    def check_winner(player):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

    current_player = "X"

    for turn in range(9):
        print_board()
        print(f"Player {current_player}'s turn")
        print("Choose position (1-9):")

        try:
            pos = int(input()) - 1
            if board[pos] != " ":
                print("⚠️ Position taken! Try again.")
                continue
        except:
            print("⚠️ Invalid input!")
            continue

        board[pos] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} Wins!")
            break

        if turn == 8:
            print_board()
            print("🤝 It's a Draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    again = input("Play again? (yes/no): ")
    if again.lower() == "yes":
        tic_tac_toe()
    else:
        print("Thanks for playing! 👋")

tic_tac_toe()