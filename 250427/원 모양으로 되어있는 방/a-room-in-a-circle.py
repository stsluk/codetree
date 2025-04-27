n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
a = a + a
min_distance = 99999999
for i in range(n):
    distance = 0
    d = 1
    for j in range(i+1, i+n):
        distance += a[j]*d
        d += 1
    min_distance = min(min_distance, distance)
print(min_distance)