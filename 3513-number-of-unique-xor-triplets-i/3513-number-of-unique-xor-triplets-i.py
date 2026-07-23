class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases for n <= 2
        if n < 3:
            return n
            
        # For n >= 3, the answer is 2^(bit_length(n))
        return 1 << n.bit_length()