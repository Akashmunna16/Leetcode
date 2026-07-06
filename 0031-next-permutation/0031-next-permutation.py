class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
                
        # If pivot exists, find the successor to swap with
        if pivot != -1:
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # Step 2: Swap pivot and successor
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
                    
        # Step 3: Reverse the elements after the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1