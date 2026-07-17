class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1: return 2**31 - 1
        
        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # Bit manipulation: Subtract shifted divisors
        for i in range(31, -1, -1):
            if (b << i) <= a:
                res += (1 << i)
                a -= (b << i)
        
        return -res if negative else res