arr = list(map(int, input().split()))

# Please write your code here.
total_arr = sum(arr)
MAX = 99999999999
ans = MAX
for i in range(5):  # team1 = arr[i]
    for j in range(4):
        for k in range(j+1, 5):
            if (j == i) or (k == i): continue
            team1 = arr[i]
            team2 = arr[j] + arr[k]
            team3 = total_arr - team1 - team2
            if (team1 != team2) and (team1 != team3) and (team2 != team3):
                ans = min(ans, max(team1, team2, team3)-min(team1, team2, team3))
if ans == MAX: print(-1)
else: print(ans)