class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # Sum elements at index 0, 2, 4, 6...
        return sum(nums[::2])