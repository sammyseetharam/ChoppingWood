class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first we need to remove all spaces, punctuation and capitalization from the string. 
        #so "Was it a car or a cat I saw?" becomes "wasitacaroracatisaw"
        normalized = self.normy(s) 
        start, end = 0, len(normalized) - 1 

        while(start < end): 
            if(normalized[start] == normalized[end]):
                start += 1
                end -= 1
            else: 
                return False 

        return True 


    def normy(self, s: str) -> str: 
        #should take in a string and strip it to barebones 
        empty = ""

        for c in s: 
            if c.isalnum(): 
                empty += (c.lower())

        return empty