# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        dist = 0
        while dist < n and fast:
            fast = fast.next 
            dist += 1 
        
        #now slow and fast are already n apart 
        while fast: 
            slow = slow.next
            fast = fast.next

        #remove lives at slow now
        slow.next = slow.next.next

        return dummy.next 

    