N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
price = [0]*N
ans_price = 999999999
total_price = 0
cnt = 0 # total_price에 몇 개의 밭의 비용을 더했는 지
for i in range(N):
    price[i] = abs(H-arr[i])
    total_price += price[i]
    if cnt < 3:
        cnt += 1
        if cnt == 3:
            ans_price = min(ans_price, total_price)
        continue
    total_price -= price[i-3]
    ans_price = min(ans_price, total_price)
print(ans_price)