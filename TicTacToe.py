# Temur Khabibullaev
# 11/3/2019
# Board And Display:

def show_display():
    print("""1 | 2 | 3
4 | 5 | 6
7 | 8 | 9\n""")


def game():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    moveX = int(input('Your move:\n>>> '))
    if moveX == 1:
        board[0] = 'X'
    if moveX == 2:
        board[1] = 'X'
    if moveX == 3:
        board[2] = 'X'
    if moveX == 4:
        board[3] = 'X'
    if moveX == 5:
        board[4] = 'X'
    if moveX == 6:
        board[5] = 'X'
    if moveX == 7:
        board[6] = 'X'
    if moveX == 8:
        board[7] = 'X'
    if moveX == 9:
        board[8] = 'X'
    first_line = board[0] + " | " + board[1] + " | " + board[2]
    second_line = board[3] + " | " + board[4] + " | " + board[5]
    third_line = board[6] + " | " + board[7] + " | " + board[8]
    print(first_line)
    print(second_line)
    print(third_line)

show_display()
game()
