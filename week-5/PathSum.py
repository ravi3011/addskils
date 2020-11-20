# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(root is None):
            return not ((sum == 0) or (sum != 0))
        else:
            ans = False
            subSum = sum - root.val
            
            if(subSum == 0  and root.left is None and root.right is None):
                return True
            if(root.left is not None):
                ans = ans or self.hasPathSum(root.left,subSum)
            if(root.right is not None):
                ans = ans or self.hasPathSum(root.right,subSum)
                
            return ans
        