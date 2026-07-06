class NumArray:
    def __init__(self, nums: List[int]):
        # Build prefix sum array padded with a leading 0
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Return computed range in O(1) time
        return self.prefix_sums[right + 1] - self.prefix_sums[left]