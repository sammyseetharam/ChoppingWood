class Solution:
    def maxArea(self, heights: List[int]) -> int:
        wuter = 0; 
        left, right = 0, len(heights) - 1
        width = 0; 

        while(left < right):
            curr = min(heights[left], heights[right]); 
            width = right - left; 
            if((curr * width) > wuter): 
                wuter = curr * width; 
            if(heights[left] < heights[right]):
                left+=1;
            elif(heights[left] > heights[right]):
                right-=1; 
            else: 
                left+=1; 
                right-=1; 

        return wuter;   