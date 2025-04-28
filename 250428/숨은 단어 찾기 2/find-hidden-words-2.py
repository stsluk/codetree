N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
def is_LEE(i, j):
    ans = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0: continue
            if judgement_EE(i, j, di, dj):
                ans += 1
    return ans


def judgement_EE(i, j, di, dj):
    for k in [1, 2]:
        y = i + di*k
        x = j + dj*k
        if not ((0<= y <N) and (0<= x <M)):
            return False
        if arr[y][x] != 'E':
            return False
    return True


ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            a = is_LEE(i, j)
            if a != 0:
                ans += a
print(ans)