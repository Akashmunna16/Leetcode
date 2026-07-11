class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        
        # Jump in blocks of 2k
        for i in range(0, len(chars), 2 * k):
            # Reverse the first k characters of the block
            chars[i:i + k] = reversed(chars[i:i + k])
            
        return "".join(chars)