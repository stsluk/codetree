n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

prices = [[0 for _ in range(n-m+1)] for _ in range(n)]
for i in range(n):
    for j in range(n-m+1):
        choose = weight[i][j:j+m]
        price = 0
        if sum(choose) <= c:
            for k in choose:
                price += k*k
        else:
            dp = [0] * (c+1)
    
            for num in choose:
                for w in range(c, num-1, -1):
                    dp[w] = max(dp[w], dp[w - num] + num * num)

            price = max(dp)
        prices[i][j] = price
max_prices = [0] + [max(prices[i]) for i in range(n)]


mr1, mr2 = 0, 0
for i in range(1, n+1):
    if max_prices[i] > max_prices[mr1]:
        mr1, mr2 = i, mr1
    elif max_prices[i] > max_prices[mr2]:
        mr2 = i

k = max_prices[mr2]

for i in range(n-m+1):
    if prices[mr1-1][i] == max_prices[mr1]:
        non_possible = {i}
        for d in range(1, m):
            non_possible.add(i+d)
            non_possible.add(i-d)
        
        for j in range(n-m+1):
            if j in non_possible: continue
            if k < prices[mr1-1][j]: k = prices[mr1-1][j]

ans = max_prices[mr1] + k
print(ans)