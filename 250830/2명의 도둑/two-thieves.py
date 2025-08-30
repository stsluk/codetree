n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

prices = [[0 for _ in range(n-1)] for _ in range(n)]
max_prices = [0]
for i in range(n):
    for j in range(n-1):
        price = 0
        a, b = weight[i][j], weight[i][j+1]
        if a + b <= c:
            price = a*a + b*b
        else:
            if a < b: a, b = b, a

            if a <= c: price = a*a
            elif b <= c: price = b*b
        prices[i][j] = price
    max_prices.append(max(prices[i]))


mr1, mr2 = 0, 0
for i in range(1, n+1):
    if max_prices[i] > max_prices[mr1]:
        mr1, mr2 = i, mr1
    elif max_prices[i] > max_prices[mr2]:
        mr2 = i

k = max_prices[mr2]

for i in range(n-1):
    if prices[mr1-1][i] == max_prices[mr1]:
        non_possible = {i-1, i, i+1}
        break

for i in range(n-1):
    if i in non_possible: continue
    if k < prices[mr1-1][i]: k = prices[mr1-1][i]

ans = max_prices[mr1] + k
print(ans)