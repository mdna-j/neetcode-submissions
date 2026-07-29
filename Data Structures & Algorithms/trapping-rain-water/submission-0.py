class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, len(height) - 1
        left_max_val, right_max_val = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max_val:
                    left_max_val = height[left]
                else:
                    water += left_max_val - height[left]
                left += 1
            else:
                if height[right] >= right_max_val:
                    right_max_val = height[right]
                else:
                    water += right_max_val - height[right]
                right -= 1
                
        return water