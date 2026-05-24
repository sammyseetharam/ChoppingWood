class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # Skip the same value to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Now it's just Two Sum!
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    # Skip duplicates for the left pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res