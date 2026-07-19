class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width and limiting height
            width = right - left
            current_height = min(heights[left], heights[right])
            
            # Update the maximum area found so far
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water