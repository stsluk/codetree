n, m, p = map(int, input().split())

# Please write your code here.
dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dic = dic[:n]
for _ in range(m):
    c, u = input().split()
    if _ < p-1: continue
    if (_ == p-1) and (u == '0'):
        dic = []
        break
    if c in dic:
        i = dic.index(c)
        del dic[i]
print(*dic)