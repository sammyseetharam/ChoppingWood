class Solution:
    def isValid(self, s: str) -> bool:
        #stack problem 
        #valid cases are either immediately closed
        #or a bunch of open and then proper corresponding closed 
        #{{{}}} or ({{[]}})
        #need to somehow find broken case "[(])"
        #so no matter what, the most recent closing should equal the most recent opening? 
        cur = 0
        stack = []

        if len(s) % 2 == 1: 
            return False 

        while cur < len(s): 
            if s[cur] == "(" or s[cur] == "[" or s[cur] == "{": 
                stack.append(s[cur])
                cur += 1
            elif len(stack) != 0: 
                if s[cur] == "}" and stack[-1] == "{": 
                    stack.pop()
                    cur += 1 
                elif s[cur] == "]" and stack[-1] == "[": 
                    stack.pop()
                    cur += 1 
                elif s[cur] == ")" and stack[-1] == "(": 
                    stack.pop()
                    cur += 1 
                else:
                    return False 
            else: 
                return False 
        
        return len(stack) == 0