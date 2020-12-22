def isBalanced(s):
    if(not s):
        return "YES"
    stack = []
    for c in s:
        if(c in ["(","[","{"]):
            stack.append(c)
        else:
            if(not stack):
                return "NO"
            temp = stack.pop()
            if(temp == '('):
                if(c != ")"):
                    return "NO"
            if(temp == "{"):
                if(c != "}"):
                    return "NO"
            if(temp == "["):
                if(c != "]"):
                    return "NO"
    if(stack):
        return "NO"
    return "YES" 