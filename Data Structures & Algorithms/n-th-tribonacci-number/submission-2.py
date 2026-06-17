class Solution:
    def tribonacci(self, n: int) -> int:
        '''
            to = 0
            t1 = 1
            t2 = t0 + t1 = 1
            t3 = t1+t2 = 2
            4 = 0+1+1+2 = t1+t2+t3 = 4
            5 = t4+t3+t2 = 7
            t(n) = t(n-1)+t(n-2)+t(n-3)

        '''
        if not n: return 0
        if n == 1 or n == 2:
            return 1
        res = [0]*(n+1)

        res[0] = 0
        res[1] = 1
        res[2] = 1
        
        for i in range(3, n+1):
            print(i, res)
            res[i] = res[i-1] + res[i-2] + res[i-3]
        return res[-1]
