n = int(input())
bombs = []
bomb_N = 0
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1: bombs.append((i, j)); bomb_N += 1
bombed = [[False for i in range(n)] for j in range(n)]
bomb_type = [5 for _ in range(bomb_N)]


def bomb(y, x, k):
    bomb_shapes = [
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    for dy, dx in bomb_shapes[k]:
        ny = y + dy; nx = x + dx
        if (0 <= ny < n) and (0 <= nx < n):
            bombed[ny][nx] = True


def calc():
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False
    
    for i in range(bomb_N):
        y, x = bombs[i]
        bomb(y, x, bomb_type[i])
    
    area = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]: area += 1
    return area


def find(cnt):
    if cnt == bomb_N:
        return calc()
    
    ans = 0
    for i in range(3):
        bomb_type[cnt] = i
        ans = max(find(cnt+1), ans)
        bomb_type[cnt] = 5
    return ans


print(find(0))