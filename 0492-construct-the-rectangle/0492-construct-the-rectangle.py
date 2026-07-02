import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start searching for Width from the square root of area downwards
        w = int(math.sqrt(area))
        
        while area % w != 0:
            w -= 1
            
        # Once a perfect divisor is found, calculate Length
        l = area // w
        return [l, w]