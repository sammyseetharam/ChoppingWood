class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #add all the letters of both to a key value hashmap where 
        #key is the letter and value is the number of times it appears
        #at the end check if theyre equal or not 
        
        if s == t: return True 
        if len(s) != len(t): return False 

        smap, tmap = {}, {} # {letter, freq}

        for letter in s: 
            if(letter in smap):  
                smap[letter] += 1 
            else: 
                smap[letter] = 1 

        for letter in t: 
            if(letter in tmap):  
                tmap[letter] += 1
            else: 
                tmap[letter] = 1
        
        return smap == tmap
        
