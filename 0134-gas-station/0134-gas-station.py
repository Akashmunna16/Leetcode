class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, a valid circuit cannot exist
        if sum(gas) < sum(cost):
            return -1
            
        start_station = 0
        current_tank = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # If tank drops below 0, the current starting point is invalid
            if current_tank < 0:
                # Reset tank and shift candidate starting index to the next station
                current_tank = 0
                start_station = i + 1
                
        return start_station