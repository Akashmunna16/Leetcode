from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counts = Counter(nums)
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
                
            for num in counts:
                if counts[num] > 0:
                    # Choose
                    counts[num] -= 1
                    current_path.append(num)
                    
                    backtrack(current_path)
                    
                    # Backtrack
                    counts[num] += 1
                    current_path.pop()
                    
        backtrack([])
        return result