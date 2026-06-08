class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k: 
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
    #we want to return the top element as the kth largest each time
        heapq.heappush(self.minHeap, val) #adding the element on
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

