class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_digits = []
        sum_of_digits = 0
        
        # Parse the integer as a string to examine characters sequentially
        for char in str(n):
            if char != '0':
                digit = int(char)
                sum_of_digits += digit
                non_zero_digits.append(char)
                
        # If no non-zero digits were collected, return 0
        if not non_zero_digits:
            return 0
            
        # Re-form the isolated non-zero digits into a fresh integer x
        x = int("".join(non_zero_digits))
        
        return x * sum_of_digits