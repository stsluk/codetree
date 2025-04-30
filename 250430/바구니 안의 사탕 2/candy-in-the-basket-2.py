N, K = map(int, input().split())
dic = [0]*101

# candy position
for _ in range(N):
    c, p = map(int, input().split())
    dic[p] += c

max_candy = 0
for i in range(101):
    if (i+2*K) > 100:
        sum_candy = sum(dic[i:101])
        max_candy = max(max_candy, sum_candy)
        break
    sum_candy = sum(dic[i:i+2*K+1])
    max_candy = max(max_candy, sum_candy)
print(max_candy)