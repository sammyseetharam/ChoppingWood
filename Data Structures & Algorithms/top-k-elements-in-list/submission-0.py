from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap to list numbers by their frequency 
        #start off with a hashmap for frequency of each element
        #then equate frequencies to indexes and append values there 
        #then sort from the bottom 

        count = defaultdict(int) #original hashmap for frequencies 

        freq = []
        for i in range (len(nums) + 1): 
            freq.append([])      

        for num in nums: 
            count[num] += 1 

        #count is now a frequency hashmap 

        for n, c in count.items(): 
            freq[c].append(n)

        result = []

        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]: 
                result.append(num)
                if len(result) == k: 
                    return result

