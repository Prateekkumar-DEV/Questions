def count_char(s):
    c = {}
    for i in "COOKOFF":
        c[i] = s.count(char)
    return c

def ans(s1, s2):
    count_s1 = count_char(s1)
    count_s2 = count_char(s2)
    
    for j in count_s1:
        if count_s2[j] < count_s1[j]:
            return "NO"
    return "YES"

s1 = input()
s2 = input()

print(ans(s1, s2))
