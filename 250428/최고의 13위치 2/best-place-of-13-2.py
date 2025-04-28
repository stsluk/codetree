n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coin = 0
for i in range(n):
    for j in range(n-2):
        for k in range(i, n):
            for l in range(n-2):
                if (i == k) and (j+2 >= l): continue
                s = sum(arr[i][j:j+3]) + sum(arr[k][l:l+3])
                max_coin = max(max_coin, s)
print(max_coin)