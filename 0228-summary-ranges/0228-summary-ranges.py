class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # Keep moving forward if the numbers are contiguous
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
                
            # Range ends here
            if start != nums[i]:
                ranges.append(f"{start}->{nums[i]}")
            else:
                ranges.append(f"{start}")
                
            i += 1  # Move to the start of the next potential range
            
        return ranges