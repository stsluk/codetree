n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n):
    sum_arr = 0
    for j in range(i, n):
        sum_arr += arr[j]
        if (sum_arr/(j-i+1)) in arr[i:j+1]:
            ans += 1
print(ans)