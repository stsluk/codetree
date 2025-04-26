R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
def jump(a, b, c, d, k):
    # initial place = [a, b]
    # final place = [c, d]
    # how many jump = k
    if k == 0:
        if grid[a][b] != grid[c-1][d-1]: return 1
        else: return 0
    
    ans = 0
    for i in range(a+1, c-k):
        for j in range(b+1, d-k):
            if grid[i][j] != grid[a][b]:
                # jump success
                ans += jump(i, j, c, d, k-1)
    return ans


ans = jump(0, 0, R, C, 2)
print(ans)