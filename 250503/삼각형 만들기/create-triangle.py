n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def is_right_triangle(a, b, c):
    if len({a[0], b[0], c[0]}) == 2 and len({a[1], b[1], c[1]}) == 2:
        return True
    return False


ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_right_triangle(points[i], points[j], points[k]):
                area = ((max({points[i][0], points[j][0], points[k][0]})-min({points[i][0], points[j][0], points[k][0]})) 
                        * (max({points[i][1], points[j][1], points[k][1]})-min({points[i][1], points[j][1], points[k][1]})))
                ans = max(ans, area)
print(ans)