class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for e in nums:
            count[e] = 1 + count.get(e, 0)

        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        a = []
        for i in range(len(freq) - 1, -1, -1):
            if len(freq[i]) != 0:
                for i in freq[i]:
                    a.append(i)
                if len(a) == k:
                    return a
        