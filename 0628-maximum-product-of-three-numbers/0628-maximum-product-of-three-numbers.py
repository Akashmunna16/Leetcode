class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Track 3 largest values
        max1 = max2 = max3 = float('-inf')
        # Track 2 smallest values
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update top 3 max values
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
                
            # Update top 2 min values
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
                
        # Compare product of 3 largest vs. 2 smallest (negative) * largest
        return max(max1 * max2 * max3, min1 * min2 * max1)