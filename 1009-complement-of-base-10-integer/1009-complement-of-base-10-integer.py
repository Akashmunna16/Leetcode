class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Base case: The complement of 0 is 1
        if n == 0:
            return 1
            
        # Find the total number of bits needed to represent n
        bit_length = n.bit_length()
        
        # Create a bitmask of all 1s matching that length
        # e.g., if length is 3, (1 << 3) - 1 inside binary space is 111
        bitmask = (1 << bit_length) - 1
        
        # XORing n with the mask flips all of its bits
        return n ^ bitmask