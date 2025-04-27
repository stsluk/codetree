n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_distance = 10000000000
for i in range(1, n-1):
    a, b = points[0]
    distance = 0
    for j in range(1, n):
        if i == j: continue
        distance += abs(x[j]-a) + abs(y[j]-b)
        a, b = points[j]
    min_distance = min(min_distance, distance)

print(min_distance)