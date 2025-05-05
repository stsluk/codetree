n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]

# Please write your code here.
if messages[p-1][1] == '0':
    print()
    exit()


no_see = [True for _ in range(n)]
see = set()
for i in range(p):
    c, u = messages[i]
    if not (i > 0 and messages[i-1][1] == u): see = set()
    see.add(c)
for c in list(see):
    no_see[ord(c)-65] = False

for i in range(p, m):
    c, u = messages[i]
    no_see[ord(c)-65] = False

for i in range(n):
    if no_see[i]:
        print(chr(i+65), end=' ')