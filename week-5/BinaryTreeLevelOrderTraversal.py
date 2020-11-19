def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root is None):
            return []
        q = []
        res = []
        q.insert(0,root)
        
        while(q != []):
            count = len(q)
            temp1 = []
            while(count != 0):
                count = count -1
                temp = q[-1]
                temp1.append(temp.val)
                q.pop()
                if(temp.left is not None):
                    q.insert(0,temp.left)
                if(temp.right is not None):
                    q.insert(0,temp.right)
            res.append(temp1)        
        return res