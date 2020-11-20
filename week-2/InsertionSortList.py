def insertionSortList(self, head: ListNode) -> ListNode:
        p_head = ListNode()
        current = head
        while(current):
            prev_node = p_head
            next_node = prev_node.next
            
            while(next_node):
                if(current.val < next_node.val):
                    break
                prev_node = next_node
                next_node = next_node.next
                
            next_iter = current.next
            current.next = next_node
            prev_node.next = current
            
            current = next_iter
        return p_head.next     
        