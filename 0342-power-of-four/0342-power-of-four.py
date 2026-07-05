class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1. Positive 
        # 2. Power of two 
        # 3. Bit is on an odd position
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0