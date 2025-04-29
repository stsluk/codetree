n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
dic = [0]*10000
for i in range(n):
    if c[i] == 'G': dic[x[i]] = 1
    else: dic[x[i]] = 2

ans = 0
for i in range(1, max(x)+1):
    ans = max(ans, sum(dic[i:i+k+1]))
print(ans)