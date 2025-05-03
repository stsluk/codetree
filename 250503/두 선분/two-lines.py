x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.
def is_intersecting(x1, x2, x3, x4):
    if x1 <= x3 <= x2: return True
    if x3 <= x1 <= x4: return True
    return False

if is_intersecting(x1, x2, x3, x4): print("intersecting")
else: print("nonintersecting")