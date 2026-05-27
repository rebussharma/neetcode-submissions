class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Build frequency for s1 and first window of s2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Helper to compare arrays
        def matches():
            return count1 == count2

        if matches():
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1      # add new char
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1  # remove old char

            if matches():
                return True

        return False