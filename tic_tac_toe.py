def tic_tac_toe():
    print("\n❌⭕ Tic Tac Toe")
    print("=" * 30)

    board = [" " for _ in range(9)]

    def print_board():
        print()
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        print()

    def check_winner(player):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

    player = "X"

    for turn in range(9):
        print_board()
        move = input(f"Player {player}, choose position (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("❌ Invalid input!")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("❌ Position already taken!")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print(f"🎉 Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board()
    print("🤝 It's a draw!")


# IMPORTANT FIX
if __name__ == "__main__":
    tic_tac_toe()