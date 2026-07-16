from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        
        # Step 1: Build prefixGcd array
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = gcd(x, mx)
        
        # Step 2: Sort the array
        prefix_gcd.sort()
        
        # Step 3: Pair smallest with largest and sum gcds
        ans = 0
        for i in range(n // 2):
            ans += gcd(prefix_gcd[i], prefix_gcd[n - i - 1])
        
        return ans
