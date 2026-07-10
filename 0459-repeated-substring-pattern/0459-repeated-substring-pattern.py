class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        # A repeated pattern must have a length <= half of the string's length
        for i in range(1, (n // 2) + 1):
            # The pattern length must be a perfect divisor of the total length
            if n % i == 0:
                # Check if repeating the prefix 'n // i' times reconstructs the string
                if s[:i] * (n // i) == s:
                    return True
                    
        return False