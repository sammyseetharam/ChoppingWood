class Solution:
    def trap(self, height: List[int]) -> int:
        #need to implelement a two pointer solution to find both of the maxes to the right and the left of each height 

        totalWater = 0; 
        left, right = 0, len(height) - 1; 
        leftMax, rightMax = 0, 0; 

        while left < right :
            
            if height[left] < height[right]: 
                if height[left] >= leftMax: 
                    leftMax = height[left]; 
                else: 
                    totalWater += leftMax - height[left]; 
                left += 1; 
            
            else: 
                if height[right] >= rightMax: 
                    rightMax = height[right]; 
                else: 
                    totalWater += rightMax - height[right]; 
                right -= 1; 
        
        return totalWater; 
