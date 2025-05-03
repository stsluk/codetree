n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 99999999999
for i in range(n):
    bigx = bigy = 0
    smallx = smally = 400000
    for j in range(n):
        if i == j: continue

        if bigx < points[j][0]: bigx = points[j][0]
        if smallx > points[j][0]: smallx = points[j][0]
        if bigy < points[j][1]: bigy = points[j][1]
        if smally > points[j][1]: smally = points[j][1]
    area = (bigx - smallx) * (bigy - smally)
    ans = min(ans, area)
print(ans)