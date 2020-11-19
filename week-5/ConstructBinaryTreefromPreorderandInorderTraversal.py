class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(not inorder):
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+rootPos],inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos + 1 :])
        
        return root
        