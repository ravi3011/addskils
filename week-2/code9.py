class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        slef.s = []    
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.insert(0,x)
        return None
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(self.s):
            return False
        else:
            return True
            
                
 