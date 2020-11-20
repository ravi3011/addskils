def isPalindrome(head):
        s = []
        temp = head
        while(temp != None):
            s.insert(0,temp.val)
            temp = temp.next
        
        temp = head
        res = True
        while(temp != None):
            p = s.pop(0)
            if(p != temp.val):
                return False
            else:
                temp = temp.next
        
        return True