class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        if len(s) < 2:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not self.isalnum(s[left]): # while left < right  need this here as left +1 below can grow and left go out og bound
                left += 1
            while right > left and not self.isalnum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    
    def isalnum(self, c: chr):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') )