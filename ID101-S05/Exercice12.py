def estPalindrome(ch:str):
    i = 0
    j = len(ch) -1
    while i < j:
        if ch[i] != ch[j]:
            return False
        i += 1
        j -= 1
    return True
def estPalindrome(ch:str):
    ch = "".join(ch.split("a"))
    return ch == ch[-1::-1]
print(estPalindrome("LAVAL"))