class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solve with a prefix and a suffix sum? 


        res = [1] * (len(nums))

        pre = 1 
        for num in range (len(nums)):
            res[num] = pre
            pre *= nums[num]

        post = 1 
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= post 
            post *= nums[i]


        return res 