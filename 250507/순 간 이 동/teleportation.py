a, b, x, y = map(int, input().split())

# Please write your code here.
# case1: a -> b
# case2: a -> x -> y -> b
# case3: a -> y -> x -> b

c1 = abs(b-a)
c2 = abs(a-x) + abs(b-y)
c3 = abs(a-y) + abs(b-x)
ans = min(c1, c2, c3)
print(ans)