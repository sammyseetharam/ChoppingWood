class Solution:
    def trap(self, height: List[int]) -> int:
        #need to implelement a two pointer solution to find both of the maxes to the right and the left of each height 

        totalWater = 0; 

        left, right = 0, len(height) - 1; 
        leftMax = 0; 
        while(left <= right):

            if(height[left] > leftMax):
                leftMax = height[left];  
            
            rightMax = 0; 
            #find the maxRight
            for i in range(len(height) - 1, left, -1):
                if(height[i] > rightMax):
                    rightMax = height[i]; 
                
            #potential calculation
            potential = min(leftMax, rightMax) - height[left]; 
            if(potential > 0): 
                totalWater += potential; 

            left += 1;


        return totalWater;  

