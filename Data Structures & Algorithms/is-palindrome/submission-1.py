class Solution:
    def isPalindrome(self, s: str) -> bool:
        lift =0
        right=len(s) - 1

        while lift < right:
            if not s[lift].isalnum():
                 lift+=1
            elif not s[right].isalnum():
                
                 right-=1
            else:
                if s[lift].lower() != s[right].lower():
                    return False

                lift += 1
                right -= 1
        
        return True
