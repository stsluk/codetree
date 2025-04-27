A = input()

# Please write your code here.
ans = 0
N = len(A)
for i in range(N-3):
    if A[i] == A[i+1] == '(':
        for j in range(i+2, N-1):
            if A[j] == A[j+1] == ')':
                ans += 1
print(ans)