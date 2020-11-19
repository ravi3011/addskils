def inorder(self,root):
    global temp
        
    if(root is None):
        return True
    if(self.inorder(root.left) is False):
        return False
    if(temp is not None and temp.val >= root.val):
        return False
    temp = root
    return self.inorder(root.right)
        
def isValidBST(self, root: TreeNode) -> bool:
    if(root is None):
        return True
        
    global temp
    temp = None
        
    return self.inorder(root)    
 