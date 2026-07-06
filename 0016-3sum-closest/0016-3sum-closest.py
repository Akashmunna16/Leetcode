class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            # Optimization: Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum  # Perfect match found
                    
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum