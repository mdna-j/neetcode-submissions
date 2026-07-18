class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # To store the indices of the days
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Check if the current temperature is warmer than the temperature at the top of the stack
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            
            # Push the current day's index onto the stack
            stack.append(curr_day)
            
        return ans
        