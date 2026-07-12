class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Get unique elements and sort them in ascending order
        sorted_unique = sorted(set(arr))
        
        # Step 2: Map each element to its rank (1-indexed)
        # enumerate(..., start=1) gives us the rank automatically
        rank_map = {num: rank for rank, num in enumerate(sorted_unique, start=1)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]