class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        high, low = max(nums), min(nums)
        if high == low:
            return 0
            
        # Compute the minimum possible size for the maximum gap boundary
        bucket_size = max(1, (high - low) // (n - 1))
        bucket_count = (high - low) // bucket_size + 1
        
        # Initialize buckets to store only min and max tracking markers
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        # Populate the buckets
        for num in nums:
            idx = (num - low) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
            
        # Scan buckets to find the maximum sequential gap difference
        max_gap = 0
        previous_max = low
        
        for i in range(bucket_count):
            # Skip empty buckets
            if buckets_min[i] == float('inf'):
                continue
                
            # Gap occurs between current bucket min and previous non-empty bucket max
            max_gap = max(max_gap, buckets_min[i] - previous_max)
            previous_max = buckets_max[i]
            
        return max_gap