X = int(input())

# Please write your code here.
v = 1
t = 0
while (X>0):
    t += 1
    X -= v
    if X >= (v+1)*(v+2)*0.5: v += 1
    elif X < v*(v+1)*0.5: v -= 1
print(t)