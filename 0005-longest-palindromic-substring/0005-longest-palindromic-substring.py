class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
            
        start = end = 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Returns the length of the valid palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Odd length center check (e.g., "aba")
            len1 = expand_around_center(i, i)
            # Even length center check (e.g., "abba")
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            # If a longer palindrome is discovered, update the global bounding box pointers
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]