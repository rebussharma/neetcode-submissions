from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)
        
        left = start = end = 0
        
        for right, char in enumerate(s):
            # If this char is needed, reduce missing
            if need[char] > 0:
                missing -= 1
            
            need[char] -= 1
            
            # When all chars are matched
            while missing == 0:
                # Update result window
                if end == 0 or right - left + 1 < end - start:
                    start, end = left, right + 1
                
                # Try to shrink from left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                
                left += 1
        
        return s[start:end]