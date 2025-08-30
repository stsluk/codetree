expression = input()

result = set()
dic = {}

def calc(k, ans):
    if k >= len(expression):
        result.add(ans)
        return 
    
    if expression[k] in dic:
        if expression[k-1] == '-':
            calc(k+2, ans - dic[expression[k]])
        elif expression[k-1] == '*':
            calc(k+2, ans * dic[expression[k]])
        else:
            calc(k+2, ans + dic[expression[k]])
    
    else:
        dic[expression[k]] = 1
        calc(k, ans)
        dic[expression[k]] = 2
        calc(k, ans)
        dic[expression[k]] = 3
        calc(k, ans)
        dic[expression[k]] = 4
        calc(k, ans)
        del dic[expression[k]]


calc(0, 0)
print(max(result))