class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check length if different doeesn't matter
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False

        return True      