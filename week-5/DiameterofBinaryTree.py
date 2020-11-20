class Height:
    def __init__(self):
        self.h = 0

class Solution:
    def diameter(self,root,height):
        
        lh = Height()
        rh = Height()
        
        if(root is None):
            height.h = 0
            return 0
        ldia = self.diameter(root.left,lh)
        rdia = self.diameter(root.right,rh)
        
        height.h = max(lh.h,rh.h) + 1
        
        return max(lh.h + rh.h, max(ldia,rdia))
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        height = Height()
        return self.diameter(root,height)