import sys
def check(strList):
    common_chars = []
    min_frequency = [sys.maxsize for _ in range(26)]
    for current_string in strList:
        chr_frequency = [0 for _ in range(26)]
        
        for c in current_string:
            chr_frequency[ord(c)-ord('a')] +=1
        for j in range(26):
            min_frequency[j] = min(min_frequency[j],chr_frequency[j])
    
    for i in range(26):
        while(min_frequency[i] > 0):
            common_chars.append(chr(i+ord('a')))
            min_frequency[i] -= 1            
    return common_chars
print(check(["bella","label","roller"]))            