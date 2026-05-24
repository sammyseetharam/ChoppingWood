# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #trying to achieve this in O(n) time and O(1) space 
        #start:  [0, 1, 2, 3]
        #finish: [3, 2, 1, 0] 
        #  p, c  
        # [n, 0, 1, 2, 3]

        # [1, 0, n, 2, 3]
        #temp = 1, prev = 1

        # [2, 1, 0, n, 3]
        
        # [3, 2, 1, 0, n]


        #take curr:
        #prev -> next; 
        #next -> prev; temp store next 

        curr, prev = head, None 
        #curr is head because thats where we start
        #prev is None because it goes null -> 0 
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 


        return prev