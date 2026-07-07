class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        # Calculate the fixed delta shift needed per candy element
        delta = (sum_bob - sum_alice) // 2
        
        # Store Bob's candy sizes in a set for O(1) lookups
        bob_set = set(bobSizes)
        
        for x in aliceSizes:
            target_y = x + delta
            if target_y in bob_set:
                return [x, target_y]