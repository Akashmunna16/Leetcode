class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            # Add the current number to all existing subsets
            result += [current + [num] for current in result]
            
        return result