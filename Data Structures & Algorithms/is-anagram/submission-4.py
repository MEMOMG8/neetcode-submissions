class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)

        if len(s) != len(t):
            return False

        for char in t:
            if count[char] > 0:
                count[char] -= 1
            else:
                return False
        return True