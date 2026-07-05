class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits needed to represent the integer
        bit_length = num.bit_length()
        
        # Create a bitmask of all 1s of the same length (e.g., if length is 3, mask is 111 in binary)
        bitmask = (1 << bit_length) - 1
        
        # XORing the number with the bitmask flips all its bits
        return num ^ bitmask