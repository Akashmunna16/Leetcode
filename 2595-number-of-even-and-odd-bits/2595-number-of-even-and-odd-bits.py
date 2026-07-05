class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even_count = 0
        odd_count = 0
        index = 0
        while n > 0:
            # If the current lowest bit is a 1
            if n & 1:
                if index % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            # Shift right to examine the next bit
            n >>= 1
            index += 1
        return [even_count, odd_count]