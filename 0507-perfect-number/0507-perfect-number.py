import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Numbers less than or equal to 1 cannot be perfect numbers
        if num <= 1:
            return False
            
        # 1 is always a proper divisor
        divisor_sum = 1
        upper_bound = int(math.sqrt(num))
        
        for i in range(2, upper_bound + 1):
            if num % i == 0:
                divisor_sum += i
                # If the paired divisor is different, add it too
                if i != num // i:
                    divisor_sum += num // i
                    
        return divisor_sum == num