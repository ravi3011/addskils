import sys
class Node:
    def __init__(self,val = None):
        self.val = val,
        self.minVal = sys.maxsize
        self.next = None
        
class MinStack:
    def __init__(self):
        self.head = Node()
        

    def push(self, x: int) -> None:
        if(self.head is None):
            self.head.next = None
            self.head.val = x
            self.minVal = x
        else:
            temp = Node()
            temp.next = self.head
            if(self.head.minVal < x):
                temp.minVal = self.head.minVal
            else:
                temp.minVal = x
            temp.val = x
            self.head = temp 
        return None               

    def pop(self) -> None:
        temp = self.head
        self.head = temp.next
        del temp
        return None
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:      
        return self.head.minVal

S = MinStack()
S.push(1)
S.push(5)
S.push(2)
S.push(6)
print(S.pop())
print(S.top())
print(S.getMin())    

