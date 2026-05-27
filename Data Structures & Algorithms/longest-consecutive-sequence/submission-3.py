class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
       # do NOT SORT
        s = set(nums)

        lcs = 0
        for n in nums:
           # check if n is the start of a sequence
           # a number is start of a sequennce if it doesn't have a left neighbor
           # 4,2,3 here 4 isn't a start of sequecne as 3 (4-1) exists 
           # 2 is start of sequqnce as 1(2-1) doesnt exits
           if (n-1) not in s:
            length = 0
            while (n + length) in s:
                length += 1
            lcs = max(length, lcs)
        return lcs