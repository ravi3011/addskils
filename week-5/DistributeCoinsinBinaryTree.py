# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def dfs(self,root):
        if(not root):
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        self.ans += abs(l) + abs(r)
        return root.val + l + r -1
    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans