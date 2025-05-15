import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
bombs = []
bombN = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))
            bombN += 1

def bomb_area(i, g):
    if i == bombN:
        return get_area(g)

    ans = 0
    a = copy.deepcopy(g)
    y, x = bombs[i]

    # case 1
    for k in range(-2, 3):
        if 0 <= y+k < n:
            a[y+k][x] = 1
    ans = max(ans, bomb_area(i+1, a[:]))
    for k in range(-2, 3):
        if 0 <= y+k < n:
            a[y+k][x] = g[y+k][x]
    
    # case 2
    for ky, kx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if (0 <= y+ky < n) and (0 <= x+kx < n):
            a[y+ky][x+kx] = 1
    ans = max(ans, bomb_area(i+1, a[:]))
    for ky, kx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if (0 <= y+ky < n) and (0 <= x+kx < n):
            a[y+ky][x+kx] = g[y+ky][x+kx]
    
    # case 3
    for ky, kx in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        if (0 <= y+ky < n) and (0 <= x+kx < n):
            a[y+ky][x+kx] = 1
    ans = max(ans, bomb_area(i+1, a[:]))
    
    return ans


def get_area(g):
    ans = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1: ans += 1
    return ans


print(bomb_area(0, grid))