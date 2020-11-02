from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        return None
        

    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        if(self.q):
            return False
        else:
            return True

s = MyStack()
s.push(2)
s.push(3)
s.push(6)
s.push(5)
print(s.pop())
print(s.top())
        