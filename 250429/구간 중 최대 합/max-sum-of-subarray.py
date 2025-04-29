n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n-k+1):
    ans = max(ans, sum(arr[i:i+k]))
print(ans)