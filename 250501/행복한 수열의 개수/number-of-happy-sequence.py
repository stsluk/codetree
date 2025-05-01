n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    # column
    c = 0
    k = grid[i][0]
    for j in range(n):
        if grid[i][j] == k:
            c += 1
            if c >= m:
                ans += 1
                break
        else:
            c = 1
            k = grid[i][j]
    
    # row
    c = 0
    k = grid[0][i]
    for j in range(n):
        if grid[j][i] == k:
            c += 1
            if c >= m:
                ans += 1
                break
        else:
            c = 1
            k = grid[j][i]
print(ans)