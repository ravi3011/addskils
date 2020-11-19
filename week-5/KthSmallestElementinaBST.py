class Solution:
    def inorder(self,root,lis):
        if(root is None):
            return None
        self.inorder(root.left,lis)
        lis.append(root.val)
        self.inorder(root.right,lis)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lis = []
        self.inorder(root,lis)
        return lis[k-1]