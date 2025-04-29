N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
x = sum(arr)
diffrent_x = x-S
ans = 9999999999999

for i in range(N-1):
    for j in range(i+1, N):
        ans = min(abs(diffrent_x-arr[i]-arr[j]), ans)
print(ans)