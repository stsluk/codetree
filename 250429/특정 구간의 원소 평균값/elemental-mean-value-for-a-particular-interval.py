n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n):
    sum_arr = 0
    scope = set()
    for j in range(i, n):
        sum_arr += arr[j]
        scope.add(arr[j])
        if (sum_arr/(j-i+1)) in scope:
            ans += 1
print(ans)