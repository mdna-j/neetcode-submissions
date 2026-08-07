class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Hash map to store numbers as keys and their indices as values
        seen = {}
        
        # Loop through the list to get both index and value
        for i, num in enumerate(nums):
            # Calculate the required number to reach the target
            complement = target - num
            
            # If the complement is already in the map, we found the pair
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index to the map
            seen[num] = i
        