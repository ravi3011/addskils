def sortList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    
    def merge(self,l1,l2):
        temp = ListNode()
        tail = temp
        while(l1 != None  and l2 != None):
            if(l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        if(l1 != None):
            tail.next = l1
        else:
            tail.next = l2
        return temp.next    
        
    
    def getMid(self,head):
        midPrev = None
        while(head != None and head.next != None):
            if(midPrev is None):
                midPrev = head
            else:
                midPrev = midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
                
        