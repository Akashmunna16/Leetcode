class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
            
        # Map indices to hex characters
        hex_chars = "0123456789abcdef"
        
        # Convert negative numbers to their 32-bit two's complement unsigned representation
        num &= 0xFFFFFFFF
        
        result = []
        while num > 0:
            # Extract the lowest 4 bits (base 16 digit)
            digit = num & 15
            result.append(hex_chars[digit])
            num >>= 4
            
        # Reverse because digits were collected from right to left
        return "".join(result[::-1])