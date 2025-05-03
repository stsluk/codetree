n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 99999999999
for i in range(n-1):
    for j in range(i+1, n):
        c = (points[i][0] - points[j][0])*(points[i][0] - points[j][0]) + (points[i][1] - points[j][1])*(points[i][1] - points[j][1])
        ans = min(ans, c)
print(ans)