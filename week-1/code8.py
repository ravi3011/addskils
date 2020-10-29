def removeElements(head, val):
        temp = head
        prev = None
        while(temp != None and temp.val == val):
            head = temp.next
            temp = head
            
        while(temp != None):
            while(temp is not None and temp.val is not val):
                prev = temp
                temp = temp.next
            if(temp == None):
                return head
            prev.next = temp.next
            temp = prev.next
        return head 