# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addSum(self,root,current,sum):
        if(not root):
            return 
        current = current*10 + root.val
        if(not root.left and not root.right):
            sum[0] += current
            return
        self.addSum(root.left,current,sum)
        self.addSum(root.right,current,sum)
        
    def sumNumbers(self, root: TreeNode) -> int:
        if(not root):
            return 0
        current = 0
        sum = [0]
        self.addSum(root,current,sum)
        return sum[0]
        