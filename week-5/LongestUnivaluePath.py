# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def dfs(self,root):
        if(root is None):
            return 0
        leftPath = self.dfs(root.left)
        rightPath = self.dfs(root.right)
        
        leftCheck = 0
        rightCheck = 0
        
        if(root.left != None and root.val == root.left.val):
            leftCheck = leftPath + 1
        if(root.right != None and root.val == root.right.val):
            rightCheck = rightPath + 1
            
        self.res = max(self.res,leftCheck+rightCheck)
        return max(leftCheck,rightCheck)
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res
        