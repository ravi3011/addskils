def check(s):
    if(s == ""):
        return False

    i = 0
    j = len(s) - 1
    s = s.lower()
    print(s)
    while(i < j):
        while(i < j and not ((s[i] >= 'a' and s[i] <= 'z') or (s[i]>= '0' and s[i] <= '9'))):
            i += 1
        while(i < j and not ((s[j] >= 'a' and s[j] <= 'z') or (s[j] >= '0' and s[j]<= '9'))):
            j -= 1

        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True            


s = "race a car"
print(check(s))

def isPalindrome(s):
    str1 = ''
    for i in s:
        if i.isalnum():
            str1 += i
    if str1.lower() == str1[::-1].lower():
        return True
    return False


