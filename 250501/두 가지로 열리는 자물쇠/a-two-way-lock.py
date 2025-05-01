N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def is_open(x, y, z, a, b, c):
    if (abs(x-a) > 2) and (N - abs(x-a) > 2): return False
    if (abs(y-b) > 2) and (N - abs(y-b) > 2): return False
    if (abs(z-c) > 2) and (N - abs(z-c) > 2): return False
    return True


ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if is_open(i, j, k, a1, b1, c1) or is_open(i, j, k, a2, b2, c2):
                ans += 1
print(ans)