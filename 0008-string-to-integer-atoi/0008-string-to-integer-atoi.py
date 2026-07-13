class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        # Step 2: Determine the sign flag
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Parse numerical characters
        result = 0
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
        # Apply sign multiplier
        result *= sign
        
        # Step 4: Handle standard 32-bit integer clipping limits
        if result < INT_MIN: return INT_MIN
        if result > INT_MAX: return INT_MAX
        
        return result