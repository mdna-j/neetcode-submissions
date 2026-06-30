class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         # Initialize two pointers at opposite ends of the array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem requires 1-indexed results
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum is too small; move the left pointer to increase it
                left += 1
            else:
                # Sum is too big; move the right pointer to decrease it
                right -= 1
                
        return []