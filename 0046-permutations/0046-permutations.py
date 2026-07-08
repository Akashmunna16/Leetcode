class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
                
            for num in nums:
                if num not in used:
                    used.add(num)
                    current_path.append(num)
                    
                    backtrack(current_path)
                    
                    # Backtrack
                    used.remove(num)
                    current_path.pop()
                    
        backtrack([])
        return result