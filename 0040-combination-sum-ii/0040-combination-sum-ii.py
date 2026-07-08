class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # Critical for grouping duplicates
        result = []
        
        def backtrack(start, current_combo, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combo))
                return
            if remaining_target < 0:
                return
                
            for i in range(start, len(candidates)):
                # Skip duplicate elements on the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                current_combo.append(candidates[i])
                backtrack(i + 1, current_combo, remaining_target - candidates[i])
                current_combo.pop() # Backtrack
                
        backtrack(0, [], target)
        return result