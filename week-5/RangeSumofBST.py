# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def dfs(self,root,l,r):
        if(root):
            if(l <= root.val <= r):
                self.ans +=root.val
            if(l < root.val):
                self.dfs(root.left,l,r)
            if(root.val < r):
                self.dfs(root.right,l,r)
                
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.dfs(root,low,high)
        return self.ans
        