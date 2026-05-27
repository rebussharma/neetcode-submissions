class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        l = 0

        for r in range(len(arr)):
            if len(res) < k:
                res.append(arr[r])
            else:
                if abs(arr[r] - x) < abs(arr[l] - x):
                    res.remove(arr[l])
                    res.append(arr[r])
                    l += 1
                elif abs(arr[r] - x) == abs(arr[l] - x):
                    print()
                    l += 1
                    continue
        return res