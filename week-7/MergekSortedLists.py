import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(not lists):
            return None
        temp = []
        for node in lists:
            while(node):
                heapq.heappush(temp,node.val)
                node = node.next
        head = ListNode(0)
        cur = head
        heapq.heapify(temp)
        while(temp):
            cur.next = ListNode(heapq.heappop(temp),None)
            cur = cur.next
            
        return head.next   
            
        