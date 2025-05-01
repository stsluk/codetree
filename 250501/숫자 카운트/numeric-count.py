n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
def is_ok(x, y, z, num, cnt1, cnt2):
    c1 = 0; c2 = 0
    nli = [x, y, z]
    num_li = list(map(int, str(num)))
    for i in range(3):
        if nli[i] == num_li[i]: c1 += 1
        elif nli[i] in num_li: c2 += 1
    
    if c1 == cnt1 and c2 == cnt2: return True
    return False


def check(x, y, z, a, b, c):
    for i in range(n):
        if not is_ok(x, y, z, a[i], b[i], c[i]):
            return False
    return True


ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i == j: continue
        for k in range(1, 10):
            if k == i or k == j: continue
            
            if check(i, j, k, a, b, c):
                ans += 1
print(ans)