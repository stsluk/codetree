n = int(input())

# Please write your code here.
def how_number(n):
    if n == 0: return 1

    ans = 0
    for i in range(1, min(5, n+1)):
        ans += how_number(n-i)
    return ans

print(how_number(n))