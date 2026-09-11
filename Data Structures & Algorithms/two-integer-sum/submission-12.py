class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store numbers and their corresponding indices
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found our pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, save the current number and its index
            seen[num] = index
            
        return []