N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
b = set(B)
ans = 0
for i in range(N-M+1):
    if set(A[i:i+M]) == b:
        ans += 1
print(ans)