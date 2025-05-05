N = int(input())
pigeon = []
position = []

# Please write your code here.
ans = 0
dic = {}
for _ in range(N):
    p, pos = map(int, input().split())
    if p in dic:
        if dic[p] != pos:
            ans += 1
    dic[p] = pos
print(ans)