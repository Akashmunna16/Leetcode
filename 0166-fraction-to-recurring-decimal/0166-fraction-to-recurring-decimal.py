class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = []
        # Handle sign
        if (numerator < 0) ^ (denominator < 0): res.append("-")
        num, den = abs(numerator), abs(denominator)
        
        res.append(str(num // den))
        rem = num % den
        if rem == 0: return "".join(res)
        
        res.append(".")
        map_rem = {} # remainder: index
        
        while rem != 0:
            if rem in map_rem:
                res.insert(map_rem[rem], "(")
                res.append(")")
                break
            map_rem[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
            
        return "".join(res)