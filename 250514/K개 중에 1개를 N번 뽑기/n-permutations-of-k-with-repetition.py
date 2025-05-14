K, N = map(int, input().split())


ans = []
def choose(n):
    if n == N:
        print(*ans)
        return 
    
    for i in range(K):
        ans.append(i+1)
        choose(n+1)
        ans.pop()


choose(0)