import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a valid repeating string divisor pattern can exist
        if str1 + str2 != str2 + str1:
            return ""
            
        # The length of the GCD string is the numerical GCD of their lengths
        gcd_len = math.gcd(len(str1), len(str2))
        
        return str1[:gcd_len]