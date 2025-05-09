n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]


# 모두 읽은 채팅이라면 읽지 않은 사람은 없습니다.
if int(messages[p - 1][1]) == 0:
    exit()

read = [False for _ in range(n)]
# 각 사람에 대해 채팅을 읽었을지 안 읽었을지 판단합니다.
# 만약 p번 메시지를 읽은 사람 수와 같은 채팅을 기준으로
# 한번이라도 채팅을 쳤다면 확실하게 채팅을 읽었습니다.
for c, u in messages:
    u = int(u)
    if u >= int(messages[p - 1][1]):
        read[ord(c) - ord('A')] = True
    
for i in range(n):
    if not read[i]:
        print(chr(ord('A') + i), end=' ')