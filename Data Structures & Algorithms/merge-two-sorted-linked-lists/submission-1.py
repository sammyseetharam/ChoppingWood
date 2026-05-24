# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #cant have any extra space complexity 
        idx1, idx2 = list1, list2
        dummy = ListNode(0) 
        curr = dummy

        while idx1 and idx2:
            if idx1.val <= idx2.val:
                curr.next = idx1    # Point the end of our new list to idx1
                idx1 = idx1.next    # Move idx1 forward
            else:
                curr.next = idx2    # Point the end of our new list to idx2
                idx2 = idx2.next    # Move idx2 forward
    
            curr = curr.next        # Move our "worker" pointer to the new end
                    
        curr.next = idx1 or idx2
        
    
        return dummy.next 