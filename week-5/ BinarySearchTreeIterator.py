# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s = []
        self.addStack(root)
        
    def addStack(self,root):
        while(root != None):
            self.s.append(root)
            root = root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp = self.s.pop()
        self.addStack(temp.right)
        return temp.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if(self.s):
            return True
        return False
