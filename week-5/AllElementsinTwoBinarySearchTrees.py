# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []
    def preOrder(self,root,l):
        if(root):
            self.preOrder(root.left,l)
            l.append(root.val)
            self.preOrder(root.right,l)
            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = []
        self.preOrder(root1,l1)
        l2 = []
        self.preOrder(root2,l1)
        
        res = l1 + l2
        res.sort()
        return res