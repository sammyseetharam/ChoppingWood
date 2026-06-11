import heapq; 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.newArr = [-s for s in stones] 
        heapq.heapify(self.newArr) 


        while (len(self.newArr) >= 2):
            x = heapq.heappop(self.newArr); 
            y = heapq.heappop(self.newArr);
            newEle = x - y; 
            if newEle != 0:
                heapq.heappush(self.newArr, newEle);

        if (len(self.newArr)) == 1: 
            return -self.newArr[0]

        return 0

