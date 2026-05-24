class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        spent = 0 
        maxLetter = 0 
        maxxer = 0 
        freq = defaultdict(int)

        if(len(s) == 1 or len(s) < k):
            return len(s)

        while r < len(s):
            freq[s[r]] += 1
            maxLetter = max(maxLetter, freq[s[r]])
            winSize = r - l + 1

            while winSize - maxLetter > k: 
                freq[s[l]] -= 1
                l += 1
                winSize = r - l + 1
            
            maxxer = max(maxxer, winSize)
            r += 1
            

        return maxxer   





