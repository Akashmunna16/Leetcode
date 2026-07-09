class Solution:
    def dayOfYear(self, date: str) -> int:
        # Parse integers directly from known string positions
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Leap year evaluation rule
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_months[1] = 29
            
        # Sum days from previous months + current month day offset
        return sum(days_in_months[:month - 1]) + day