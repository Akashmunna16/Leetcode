import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Step 1: Find the minimum and maximum elements in a single O(n) pass
        min_num = min(nums)
        max_num = max(nums)
        
        # Step 2: Return the Greatest Common Divisor of the two numbers
        return math.gcd(min_num, max_num)