n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dic = [0]*101
for x1, x2 in segments:
    for i in range(x1, x2+1):
        dic[i] += 1

if max(dic) >= n: print("Yes")
else: print("No")