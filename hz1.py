board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  #игровое поле


def board_pool():  #игровое поле
    print("▂" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "▌") * 3)
        print("", board[i * 3], "▌", board[i * 3 + 1], "▌", board[i * 3 + 2], "▌")
        print(("▂" * 3 + "▌") * 3)


def check_step(index, char):  #анализ шагов
    if index > 9 or index < 1 or board[index - 1] in ("X", "O"):
        return False

    board[index - 1] = char
    return True


def check_win():  #анализ выигрыша
    win = False

    win_combo = (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)

    for pos in win_combo:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]

    return win


def start_game():
    player_use = "X"
    step = 1
    board_pool()

    while (step < 10) and (check_win() == False):
        index = input("игрок " + player_use + " введите номер поля: ")

        if (index == "0"):
            break

        if (check_step(int(index), player_use)):
            print("успешный ход")

            if (player_use == "O"):
                player_use = "X"
            else:
                player_use = "O"

            board_pool()
            step += 1
        else:
            print("Номер неверный")

    if (step == 10):
        print("НИЧЬЯ")
    else:
        print("ВЫИГРАЛ: " + check_win())


print("КРЕСТИКИ-НОЛИКИ")
start_game()
