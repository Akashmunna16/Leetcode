class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []
        
        # Determine the digit length boundaries
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate through all possible lengths of sequential numbers
        for length in range(min_len, max_len + 1):
            # Slide the window across the master "123456789" string
            for start in range(10 - length):
                substring = sample[start : start + length]
                num = int(substring)
                
                # Check if the number falls within the target range
                if low <= num <= high:
                    result.append(num)
                    
        return result