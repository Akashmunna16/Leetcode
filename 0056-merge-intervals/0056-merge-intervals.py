class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        # Sort intervals by their starting boundary times
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last_interval = merged[-1]
            
            # If current interval overlaps with the previous one, merge them
            if current[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], current[1])
            else:
                # No overlap, append current interval as a standalone entry
                merged.append(current)
                
        return merged