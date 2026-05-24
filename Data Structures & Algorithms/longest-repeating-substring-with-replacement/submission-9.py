class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        spent = 0 
        maxLetter = 0 
        maxxer = 0 
        freq = defaultdict(int)

        while r < len(s):
            #adding up the counts 
            freq[s[r]] += 1
            maxLetter = max(maxLetter, freq[s[r]])
            winSize = r - l + 1

            #this is only the invalid case 
            while winSize - maxLetter > k: 
                freq[s[l]] -= 1
                l += 1
                winSize = r - l + 1
            
            #continously recomputing the max 
            maxxer = max(maxxer, winSize)
            r += 1
            

        return maxxer   





