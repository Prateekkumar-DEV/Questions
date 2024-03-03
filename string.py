alpha = ['C','O','K','F']

def aplha_true(s):
    case_1 = False
    for i in s:
        if i not in alpha:
            case_1 = False
        else:
            case_1 = True
    return case_1
    
def count_char(s):
    count = 0
    for i in s:
        count = count + 1
    return count

def count_check(x,y):
    case = False
    if (count_char(x) % count_char(y)) == 0:
        n = count_char(x) / count_char(y)
        for i in alpha:
            if x.count(i) == n:
                case = True
    return case
    
def check(a, b):
    if (aplha_true(a) & aplha_true(b)) == False:
        case_2 = False
    
    case_2 = count_check(s1,s2)
    
    return case_2

s1 = input().upper()
s2 = input().upper()

if check(s1,s2) == True:
    ans = "Yes"
else:
    ans = "No"

print(ans)
