class Solution:

    "Hello", "World"
    def encode(self, strs: List[str]) -> str:
        #for the encode, can we sandwich each string between two delimitters? 
        string = ""
        for elem in strs:
            string += str(len(elem)) + "#" + elem
        return string

    #"Hello*5*World*5*"
    def decode(self, s: str) -> List[str]:
        arr = []

        i = 0

        while i < len(s): 
            j = i 
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            arr.append(s[i:j])
            i = j 

        return arr