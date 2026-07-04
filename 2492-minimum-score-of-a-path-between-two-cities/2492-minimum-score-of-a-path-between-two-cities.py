from collections import deque, defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the bidirectional graph
        graph = defaultdict(list)
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))
            
        # Step 2: Initialize BFS structures
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        # Step 3: Traverse the connected component containing node 1
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Every edge attached to a reachable node is a candidate
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score