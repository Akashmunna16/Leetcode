class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Pair score with its original index and sort descending by score
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        result = [""] * len(score)
        
        for rank, (original_idx, _) in enumerate(sorted_scores, start=1):
            if rank == 1:
                result[original_idx] = "Gold Medal"
            elif rank == 2:
                result[original_idx] = "Silver Medal"
            elif rank == 3:
                result[original_idx] = "Bronze Medal"
            else:
                result[original_idx] = str(rank)
                
        return result