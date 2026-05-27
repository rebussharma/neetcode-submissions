class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        t = len(nums1) + len(nums2)
        h = t // 2

        # just a trick to make sure A is always the smaller array
        # as we need to run BS in smaller array
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True: # we're guranteed median
            i = (l + r) // 2 # for A
            j = h - i - 2 # i and j both will start at 0

            al = A[i] if i >=0 else float("-infinity")
            ar = A[i+1] if (i + 1) < len(A) else float("infinity")

            bl = B[j] if j >=0 else float("-infinity")
            br = B[j+1] if (j+1) < len(B) else float("infinity")

            if al <= br and bl <= ar:
                if t % 2: # odd
                    return min(ar, br)
                return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                r = i - 1
            else:
                l = i + 1
        
        