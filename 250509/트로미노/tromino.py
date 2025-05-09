n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def bluck_max(y, x):
    # L, I max
    ans = grid[y][x]
    arr = [grid[y][x-1] if x > 0 else 0, 
                grid[y-1][x] if y > 0 else 0, 
                grid[y][x+1] if x < m-1 else 0, 
                grid[y+1][x] if y < n-1 else 0]
    k = {arr[0]+arr[1], arr[1]+arr[2], arr[2]+arr[3], arr[3]+arr[0], arr[0]+arr[2], arr[1]+arr[3]}
    ans += max(k)
    return ans


ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, bluck_max(i, j))
print(ans)