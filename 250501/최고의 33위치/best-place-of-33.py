n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n-2):
    for j in range(n-2):
        total = 0
        for y in range(i, i+3):
            for x in range(j, j+3):
                total += grid[y][x]
        ans = max(ans, total)
print(ans)