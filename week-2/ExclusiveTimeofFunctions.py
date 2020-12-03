class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0 for _ in range(n)]
        s = logs[0].split(":")
        stack.append(int(s[0]))
        i = 1
        prev = int(s[2])
        while(i < len(logs)):
            s = logs[i].split(":")
            if(s[1] == "start"):
                if(stack):
                    res[stack[-1]] += (int(s[2]) - prev)
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                res[stack[-1]] += (int(s[2]) - prev + 1)
                stack.pop()
                prev = int(s[2]) + 1
            i += 1
        return res    
        
        