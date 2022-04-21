from connect_four import ConnectFour


def main():
    game = ConnectFour()
    while not game.is_game_over():
        print(game)
        move = input(game.whose_turn() + "'s turn, Please enter \
column 1 to 7: ").strip().lower()
        if move == 'q':
            break
        try:
            game.add_piece(int(move))
            print(game)
            undo_choice = input("Do you want to undo the step [Y/N]? ").lower()
            if undo_choice == 'y':
                game.undo()
                print("operation canceled!")
            game.is_win()
        except Exception as e:
            print(e)

    # End the game if there is a winner
    print("Final state:")
    print(game)
    print("Game Over")

    winner = game.get_winner()
    if winner in ['X', 'O']:
        print("Winner is " + winner)

    if game.is_full():
        print("The game is a draw..")


if __name__ == "__main__":
    main()
