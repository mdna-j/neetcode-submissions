class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to easily handle duplicates and use two pointers
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # If the current minimum number is greater than 0, 
            # no three numbers can ever sum up to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # We need a larger sum, move left pointer right
                elif total > 0:
                    right -= 1  # We need a smaller sum, move right pointer left
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers forward and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res
        