def lenPalandrome(s):
    out=''
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            s1 = s[i:j]
            if s1 == s1[-1::-1] and len(s1) > len(out):
                out = s1
    return len(out)
def allRetation(s):
    L =[]
    for i in range(len(s)):
        l=list(s)
        L.append(lenPalandrome("".join(l[1:] + l[0:1])))
    return L
n = int(input())
strings =allRetation(input()) 
for s in strings:
    print(s)