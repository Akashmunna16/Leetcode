class Solution:
    def intToRoman(self, num: int) -> str:
        # Group unique subtraction mappings together with baseline tokens descending
        roman_mappings = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in roman_mappings:
            if num == 0:
                break
                
            # Determine how many times this token fits into our remainder number pool
            count = num // value
            if count > 0:
                result.append(symbol * count)
                num %= value
                
        return "".join(result)