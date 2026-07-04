class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def nSum(l, r, target, N, path, result):
            if r - l + 1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return # Early pruning boundaries
            if N == 2: # Base case: Two Pointers
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        result.append(path + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: l += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1
                        r -= 1
                    elif total < target: l += 1
                    else: r -= 1
            else:
                for i in range(l, r + 1):
                    if i > l and nums[i] == nums[i - 1]: continue
                    nSum(i + 1, r, target - nums[i], N - 1, path + [nums[i]], result)

        res = []
        nSum(0, len(nums) - 1, target, 4, [], res)
        return res