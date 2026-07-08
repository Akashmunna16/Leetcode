class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, current_combo, current_sum):
            if current_sum == target:
                result.append(list(current_combo))
                return
            if current_sum > target or i >= len(candidates):
                return
                
            # Choice 1: Include candidates[i] and stay at index i (allows reuse)
            current_combo.append(candidates[i])
            backtrack(i, current_combo, current_sum + candidates[i])
            current_combo.pop() # Backtrack
            
            # Choice 2: Skip candidates[i] and move to the next index
            backtrack(i + 1, current_combo, current_sum)
            
        backtrack(0, [], 0)
        return result