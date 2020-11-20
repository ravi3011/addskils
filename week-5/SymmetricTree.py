class Solution:
    def check(self,root1,root2):
        if(root1 is None and root2 is None):
            return True
        
        if(root1 is not None and root2 is not None):
            if(root1.val == root2.val):
                return (self.check(root1.left,root2.right) and self.check(root1.right, root2.left))
        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)