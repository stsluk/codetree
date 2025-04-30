n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
dic = [' ']*101
for i in range(n):
    dic[pos[i]] = alpha[i]


max_len = 0
for i in range(101):
    if dic[i] == ' ': continue
    G_count = 0
    H_count = 0
    for j in range(i, 101):
        if dic[j] == 'G': G_count += 1
        elif dic[j] == 'H': H_count += 1
        else: continue
        
        if (H_count == 0) or (G_count == 0) or (H_count == G_count):
            max_len = max(max_len, j-i)
print(max_len)