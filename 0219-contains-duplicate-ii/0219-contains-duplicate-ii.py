class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Map to store number -> its latest index
        num_map = {}
        
        for i, num in enumerate(nums):
            if num in num_map and i - num_map[num] <= k:
                return True
            # Always update to the newest index for future checks
            num_map[num] = i
            
        return False