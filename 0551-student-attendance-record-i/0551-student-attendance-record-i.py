class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if there are 2 or more 'A's OR if there are 3 consecutive 'L's
        return s.count('A') < 2 and "LLL" not in s