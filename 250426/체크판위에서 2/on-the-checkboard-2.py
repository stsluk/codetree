R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
ans = 0

# k = 0
for i in range(1, R-2):
    for j in range(1, C-2):
        if grid[i][j] != grid[0][0]:
            # one_jump = [i, j]
            for k in range(i+1, R-1):
                for l in range(j+1, C-1):
                    if grid[k][l] != grid[i][j]:
                        # two_jump = [k, l]
                        if grid[k][l] != grid[R-1][C-1]:
                            ans += 1
print(ans)