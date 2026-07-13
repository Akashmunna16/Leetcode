class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        # Case 1: Strings are already equal
        if s == goal:
            # We need at least one duplicate character to swap harmlessly
            return len(set(s)) < len(s)
            
        # Case 2: Strings are different, gather mismatched pairs
        pairs = []
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                pairs.append((c1, c2))
                if len(pairs) > 2:
                    return False  # More than 2 mismatches can't be fixed in 1 swap
                    
        # Must be exactly 2 mismatches, and they must be cross-equal (e.g., ('a', 'b') and ('b', 'a'))
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]