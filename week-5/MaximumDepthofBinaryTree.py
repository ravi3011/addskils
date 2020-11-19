def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
        if(l > r):
            return l + 1
        else:
            return r + 1
