import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap it 
        #pop off for a K number of times 
        #return the Kth one 

        self.newArr = [-s for s in nums]
        heapq.heapify(self.newArr)
        curr = 0 

        while self.newArr and curr < k - 1: 
            heapq.heappop(self.newArr)
            curr += 1 

        heapq.heapify(self.newArr)

        return -self.newArr[0]
