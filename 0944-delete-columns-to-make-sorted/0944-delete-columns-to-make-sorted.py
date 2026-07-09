class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        
        # zip(*strs) groups strings column by column
        for column in zip(*strs):
            # Check if the column characters are sorted
            if list(column) != sorted(column):
                delete_count += 1
                
        return delete_count