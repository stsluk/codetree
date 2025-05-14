n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def large(y, x):
    ans = 0
    s = [grid[y][x], 0, 0, 0]
    for k1 in range(1, n-x):
        if (x+k1 >= n) or (y-k1 < 0): break
        s[0] += grid[y-k1][x+k1]
        s[1] = s[0]
        for k2 in range(1, n):
            if (x+k1-k2 < 0) or (y-k1-k2 < 0): break
            s[1] += grid[y-k1-k2][x+k1-k2]
            s[2] = s[1]
            for k3 in range(1, n):
                if (x+k1-k2-k3 < 0) or (y-k1-k2+k3 >= n): break
                s[2] += grid[y-k1-k2+k3][x+k1-k2-k3]
                s[3] = s[2]
                for k4 in range(1, n):
                    if (x+k1-k2-k3+k4 > x) or (y-k1-k2+k3+k4 > y): break
                    elif (k1-k2-k3+k4 == 0) and (-k1-k2+k3+k4 == 0):
                        ans = max(ans, s[3]); break
                    s[3] += grid[y-k1-k2+k3+k4][x+k1-k2-k3+k4]
    return ans


ans = 0
for i in range(2, n):
    for j in range(1, n-1):
        ans = max(ans, large(i, j))
print(ans)