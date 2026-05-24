# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split two lists
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        #at this point, fast will be at the end and then slow 
        #will be at the mid point 

        # [0, 1, 2, 3 (slow), 4, 5, 6 (fast)]

        #reverse second 
        curr = slow.next
        prev = slow.next = None
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        #combine first and second 
        idx1, idx2 = head, prev
        while idx2: 
            temp1, temp2 = idx1.next, idx2.next
            idx1.next = idx2
            idx2.next = temp1 
            idx1, idx2 = temp1, temp2



