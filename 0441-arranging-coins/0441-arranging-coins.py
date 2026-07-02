class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            # Calculate total coins needed for 'mid' complete rows
            coins_needed = (mid * (mid + 1)) // 2
            
            if coins_needed == n:
                return mid  # Perfect match found
            elif coins_needed < n:
                result = mid  # 'mid' rows can be fully built; save as a candidate
                left = mid + 1  # Try to build more rows
            else:
                right = mid - 1  # Too many coins needed; try fewer rows
                
        return result