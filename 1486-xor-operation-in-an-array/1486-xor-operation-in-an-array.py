class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Helper function to compute XOR from 1 to x in O(1) time
        def get_xor_to_x(x):
            rem = x % 4
            if rem == 0: return x
            if rem == 1: return 1
            if rem == 2: return x + 1
            return 0

        # Helper function to get XOR sum of a range [low, high]
        def get_xor_range(low, high):
            return get_xor_to_x(low - 1) ^ get_xor_to_x(high)

        # Shift everything right by 1 to form a continuous sequence of integers
        shifted_start = start >> 1
        shifted_end = shifted_start + n - 1
        
        # Calculate the XOR sum of the continuous block in O(1)
        shifted_xor_sum = get_xor_range(shifted_start, shifted_end)
        
        # Determine the least significant bit (LSB)
        # The LSB is 1 only if 'start' is odd AND 'n' is odd
        lsb = (start & 1) & (n & 1)
        
        # Shift the sum back left and merge with the computed LSB
        return (shifted_xor_sum << 1) | lsb