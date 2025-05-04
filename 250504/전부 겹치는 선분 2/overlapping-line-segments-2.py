n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def judge(dic, seg):
    for x1, x2 in seg:
        test = dic[:]
        for i in range(x1, x2+1):
            test[i] -= 1
        if max(test) >= n-1:
            return True
    return False


dic = [0]*101
# 제거하기 전
for x1, x2 in segments:
    for i in range(x1, x2+1):
        dic[i] += 1

if judge(dic, segments): print("Yes")
else: print("No")