a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if a > c: a, b, c, d = c, d, a, b

if b < c:
    ans = (b-a) + (d-c)
else:
    ans = d-a
print(ans)