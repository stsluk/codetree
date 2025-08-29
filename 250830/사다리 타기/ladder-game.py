n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 사다리 타기 결과 구하
def ladder_game(edges):
    # 사다리 타기 그리기
    ladder = [[False for _ in range(n+1)] for _ in range(m)]
    for a, b in edges:
        ladder[b-1][a] = True
    
    ans = []
    for i in range(n):
        for j in range(m):
            if ladder[j][i]: i -= 1
            elif ladder[j][i+1]: i += 1
        ans.append(i+1)
    return ans

def minimum_line(want, x, y, ans):
    if want == [1, 2, 3, 4]: return ans

    next_x = x + 1
    next_y = y
    if next_x >= n:
        next_x = 1; next_y += 1
        if next_y >= m: return 99999999
    a = minimum_line(want, next_x, next_y, ans)

    next_x = x + 2
    next_y = y
    if next_x >= n:
        next_x = 1; next_y += 1
        if next_y >= m: return 99999999
    check_want(x, want)
    a = min(a, minimum_line(want, next_x, next_y, ans+1))
    check_want(x, want)

    return a


def check_want(x, want):
    for i in range(n):
        if want[i] == x: want[i] = x+1
        elif want[i] == x+1: want[i] = x


want = ladder_game(edges)
print(minimum_line(want, 1, 0, 0))