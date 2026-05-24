class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        curr = set() 
        maxxy = 1
        incr = 0 

        if(len(s) == 0):
            return 0 

        while r < len(s) and l < len(s): 
            if s[r] not in curr: 
                incr += 1
                curr.add(s[r])
                r += 1
                maxxy = max(incr, maxxy)
            else: 
                maxxy = max(incr, maxxy)
                incr -= 1
                curr.add(s[r])
                curr.remove(s[l])
                l += 1
        

        return maxxy

