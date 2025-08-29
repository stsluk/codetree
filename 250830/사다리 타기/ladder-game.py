import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(key=lambda x:x[1])


def check_result(x, li):
    li[x], li[x-1] = li[x-1], li[x]

r = [999999999]
def optimization(k, ans):
    if a == want: r[0] = min(ans, r[0])
    if k >= m: return 

    check_result(edges[k][0], a)
    optimization(k+1, ans+1)
    check_result(edges[k][0], a)
    optimization(k+1, ans)


want = [i+1 for i in range(n)]
for x, y in edges:
    check_result(x, want)
a = [i+1 for i in range(n)]
optimization(0, 0)

print(r[0])