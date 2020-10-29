def reverseList(head):
        
        prev = None
        curr = head
        
        while(curr!=None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev 