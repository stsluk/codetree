n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def best_mining(i, j):
    ans = grid[i][j]
    gold = grid[i][j]
    for k in range(1, n):
        for l in range(k):
            if (0 <= i-k+l < n) and (0 <= j-l < n):
                gold += grid[i-k+l][j-l]
        for l in range(k):
            if (0 <= i+l < n) and (0 <= j-k+l < n):
                gold += grid[i+l][j-k+l]
        for l in range(1, k+1):
            if (0 <= i-k+l < n) and (0 <= j+l < n):
                gold += grid[i-k+l][j+l]
        for l in range(1, k+1):
            if (0 <= i+l < n) and (0 <= j+k-l < n):
                gold += grid[i+l][j+k-l]
        if gold*m - (k*k + (k+1)*(k+1)) > 0:
            ans = gold
    return ans


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, best_mining(i, j))
        # print(i, j, ':', best_mining(i, j))
print(ans)