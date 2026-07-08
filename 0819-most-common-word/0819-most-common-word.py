import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Replace all punctuation with a space and convert to lowercase
        normalized_str = re.sub(r'[^a-zA-Z0-9]', ' ', paragraph).lower()
        words = normalized_str.split()
        
        banned_set = set(banned)
        word_counts = Counter()
        
        for word in words:
            if word not in banned_set:
                word_counts[word] += 1
                
        # Return the most common unbanned word
        return word_counts.most_common(1)[0][0]