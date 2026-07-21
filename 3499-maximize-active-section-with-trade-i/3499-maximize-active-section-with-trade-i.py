class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Step 1: Count total original '1's
        total_ones = s.count('1')
        
        # Step 2: Parse string into lengths of consecutive character blocks
        zero_blocks = []
        i = 0
        n = len(s)
        
        # We can track adjacent 0-blocks separated by a single 1-block
        max_merged_zeros = 0
        prev_zero_len = 0
        has_zero = False
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            
            if s[i] == '0':
                has_zero = True
                # If there was a previous 0-block, check the sum of adjacent 0-blocks
                if prev_zero_len > 0:
                    max_merged_zeros = max(max_merged_zeros, prev_zero_len + length)
                prev_zero_len = length
            # If s[i] == '1', prev_zero_len stays intact to pair with the next 0-block
            
            i = j
            
        # Return total ones plus the best gain from merging two adjacent zero blocks
        return total_ones + max_merged_zeros