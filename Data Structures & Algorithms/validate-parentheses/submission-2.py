class Solution:
    def isValid(self, s: str) -> bool:
        STACK = [];
        
        for i in s:
            if i in ["[","{","("]:
                STACK.append(i)
            elif i in ["]","}",")"]:
                if not STACK:
                    return False
                if i=="]" and STACK[-1]=="[":
                    STACK.pop()
                elif i==")" and STACK[-1]=="(":
                    STACK.pop()
                elif i=="}" and STACK[-1]=="{":
                    STACK.pop()
                else :
                    return False
        
        return not STACK

        