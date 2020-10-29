def deleteDuplicates(head):
        temp = head
        if(temp is None):
            return
        while(temp.next is not None):
            if(temp.val == temp.next.val):
                last = temp.next.next
                temp.next = None
                temp.next = last
            else:
                temp = temp.next
        return head     