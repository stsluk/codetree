N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
B.sort()
ans = 0
for i in range(N-M+1):
    if sorted(A[i:i+M]) == B:
        ans += 1
print(ans)