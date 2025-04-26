a = input()

# Please write your code here.
i_0 = a.find('0')
a = list(a)
if i_0 == -1:
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1':
            a[i] = '0'
            break
else: a[i_0] = '1'

n = ''.join(a)
print(int(n, 2))