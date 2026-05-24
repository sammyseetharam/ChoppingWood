# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first get pointers in position 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next #single increment on the slow 
            fast = fast.next.next #double increment on the fast 
        
        #reverse a linked list
        secondHalf = slow.next
        prev = slow.next = None
        while secondHalf: 
            tmp = secondHalf.next #save the next into a temp pointer
            secondHalf.next = prev #set the next equal to the old previous
            prev = secondHalf #set the previous equal to the old second
            secondHalf = tmp   #move ahead 

        first, second = head, prev 
        while second: 
            tmp1, tmp2 = first.next, second.next #before modify
            first.next = second #modify
            second.next = tmp1 #modify 
            first, second = tmp1, tmp2 #reel it back in after modiy 


        



        