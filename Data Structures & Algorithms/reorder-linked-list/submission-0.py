class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # 1. Count total nodes
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        # 2. We only need to "pull" nodes from the back length // 2 times
        curr_front = head
        for i in range(length // 2):
            # 3. Find the node BEFORE the last node (the tail's parent)
            # We need the parent so we can set parent.next = None
            prev_to_tail = curr_front
            while prev_to_tail.next and prev_to_tail.next.next:
                prev_to_tail = prev_to_tail.next
            
            # 4. Extract the tail
            tail = prev_to_tail.next
            prev_to_tail.next = None # Cut the tail off
            
            # 5. Insert tail after curr_front
            next_front = curr_front.next
            curr_front.next = tail
            tail.next = next_front
            
            # 6. Move curr_front two steps forward (to the next 'original' node)
            curr_front = next_front