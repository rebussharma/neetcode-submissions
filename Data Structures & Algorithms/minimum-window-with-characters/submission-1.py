class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, count_t = {}, {}
        res = [-1, -1]
        res_len = float('inf')
        l = 0
        
        for n in t:
            count_t[n] = 1 + count_t.get(n, 0)
        
        have = 0
        need = len(count_t)
        
        for r in range(len(s)):
            # current char
            c = s[r]
            window[c] = 1 + window.get(c, 0)
        
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                # update minimum res
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                
                # pop from left most while condition is met
                window[s[l]] -= 1
                
                # since we pop, its possible we are not meeting condition
                # so we need to check again

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""