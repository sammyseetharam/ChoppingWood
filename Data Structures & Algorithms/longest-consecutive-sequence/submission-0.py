class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #is there a way to store the +1 elements in a hashmap 
        #hashmap should be O(n)
        #return the element with the longest length, CAN BE STORED AS A KEY      

        #checks if the value is in the hashmap 

        sequence = set(nums) 
        maxy = 0 

        for num in sequence: 
            if (num - 1) not in sequence: 
                longest = 1
                while (num + longest) in sequence: 
                    longest += 1
                maxy = max(longest, maxy)

        return maxy
