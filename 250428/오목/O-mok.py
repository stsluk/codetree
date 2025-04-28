board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def who_is_win(i, j):
    win = board[i][j]
    if win == 0: return False, False, False
    for ki in [0, 1]:
        for kj in [-1, 0, 1]:
            if ki == kj == 0: continue
            if judgement_win(i, j, ki, kj):
                return win, (i + 2*ki +1), (j + 2*kj +1)
    return False, False, False


def judgement_win(i, j, ki, kj):
    for k in range(1, 5):
        x = i + ki*k
        y = j + kj*k
        if not ((0 <= x < 19) and (0 <= y < 19)):
            return False
        if board[i][j] != board[x][y]:
            return False
    return True


def print_winner():
    for i in range(19):
        for j in range(19):
            win, x, y = who_is_win(i, j)
            if win:
                print(win)
                print(x, y)
                return 
    print(0)
    return 


print_winner()