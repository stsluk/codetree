n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
run_people = 0
for i in range(n):
    if B[i] <= A[i]:
        run_people += A[i] - B[i]
    else:
        run_people -= B[i] - A[i]
    ans += run_people

print(ans)