class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        mid = l + ((r - l) // 2)


        while l <= r: 
            if target == nums[r]: 
                return r
            if target == nums[l]: 
                return l

            if target < nums[mid]:
                r = mid
                mid = l + ((r - l) // 2)
                l += 1
            elif target > nums[mid]: 
                l = mid
                mid = l + ((r - l) // 2)
                r -= 1
            else: 

                return mid 

        return -1 