class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Map choice -> index for list1
        restaurant_map = {restaurant: idx for idx, restaurant in enumerate(list1)}
        
        result = []
        min_sum = float('inf')
        
        for idx2, restaurant in enumerate(list2):
            if restaurant in restaurant_map:
                idx1 = restaurant_map[restaurant]
                current_sum = idx1 + idx2
                
                # Found a new lowest index sum combination
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]  # Reset list with the new best choice
                # Tied with the current lowest index sum
                elif current_sum == min_sum:
                    result.append(restaurant)
                    
        return result