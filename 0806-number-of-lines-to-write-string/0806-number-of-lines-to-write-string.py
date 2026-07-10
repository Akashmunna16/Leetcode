class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0
        
        for char in s:
            char_width = widths[ord(char) - 97]
            
            if current_width + char_width > 100:
                # Wrap to a new line
                lines += 1
                current_width = char_width
            else:
                current_width += char_width
                
        return [lines, current_width]