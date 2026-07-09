from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize common counts with the frequency map of the first word
        common_counts = Counter(words[0])
        
        # Intersect with the character counts of all subsequent words
        for word in words[1:]:
            common_counts &= Counter(word)
            
        # Expand keys into list entries based on their final intersected frequencies
        return list(common_counts.elements())