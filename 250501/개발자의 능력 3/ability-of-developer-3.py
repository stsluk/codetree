abilities = list(map(int, input().split()))

# Please write your code here.
total = sum(abilities)
def get_diff(a, b, c):
    x = abilities[a] + abilities[b] + abilities[c]
    y = total - x
    return abs(x-y)


ans = 999999999
for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            ans = min(ans, get_diff(i, j, k))
print(ans)