class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):
    s = ""
    while(l1):
        s = str(l1.val)+s
        l1 = l1.next
    s1 = ""    
    while(l2):
        s1 =str(l2.val)+s1
        l2 = l2.next
        
    add = int(s) + int(s1)
    add = str(add)[::-1]
    node = None
    head = None
        
    for e in add:
        if(node is None):
            node = ListNode(int(e))
            head = node
        else:
            node.next = ListNode(int(e))
            node = node.next
    return head      


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

temp = addTwoNumbers(l1,l2)
while(temp):
    print(temp.val,end=", ")
    temp = temp.next
print()    
