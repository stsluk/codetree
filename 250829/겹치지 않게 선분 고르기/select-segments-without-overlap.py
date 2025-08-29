n = int(input())
li = []

for _ in range(n):
    a, b = map(int, input().split())
    li.append([a, b])



check_line = [False for _ in range(1001)]

def choose(li, ans):
    if not li:
        return ans

    a = li.pop()
    m = choose(li, ans)
    if is_choose(*a):
        origin = check_line[a[0]:a[1]+1]
        check_line[a[0]:a[1]+1] = [True] * (a[1]-a[0]+1)
        m = max(m, choose(li, ans+1))
        check_line[a[0]:a[1]+1] = origin
    li.append(a)

    return m
    

def is_choose(a, b):
    for i in range(a, b+1):
        if check_line[i]:
            return False
    return True

print(choose(li, 0))