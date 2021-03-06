class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if(not nums):
            return None
        
        mid = int(len(nums)/2)
        
        node  = TreeNode(nums[mid])
        
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node