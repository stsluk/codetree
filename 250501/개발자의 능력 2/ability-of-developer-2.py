ability = list(map(int, input().split()))

# Please write your code here.
def team_comp(arr):
    total_arr = sum(arr)
    mini = total_arr
    for i in range(3):
        for j in range(i+1, 4):
            t1 = arr[i] + arr[j]
            t2 = total_arr - t1
            if abs(t1-t2) < mini:
                x = t1
                y = t2
                mini = abs(t1-t2)
    return x, y


total_ability = sum(ability)
t = {0, 1, 2, 3, 4, 5}
ans = 99999999999
for i in range(5):
    for j in range(i+1, 6):
        # team1 = (ability[i], ability[j])
        team1 = ability[i] + ability[j]
        team2, team3 = team_comp([ability[k] for k in list(t-{i, j})])
        ans = min(ans, max(team1, team2, team3)-min(team1, team2, team3))
print(ans)