# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        #slow and fast pointers return true if the meet? 
        slow, fast = head, head 

        while fast and fast.next: 
            if slow: 
                fast = fast.next
                fast = fast.next
                slow = slow.next
            if fast == slow: 
                return True 

        return False 

                        
