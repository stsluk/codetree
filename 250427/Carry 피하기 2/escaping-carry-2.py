n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def is_not_carry(a, b, c):
    while (a+b+c) != max(a, b, c):
        if (a%10) + (b%10) + (c%10) >= 10:
            return False
        a //= 10; b //=10; c //= 10
    return True

max_sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_not_carry(arr[i], arr[j], arr[k]):
                max_sum = max(max_sum, arr[i]+arr[j]+arr[k])

if max_sum == 0: print(-1)
else: print(max_sum)