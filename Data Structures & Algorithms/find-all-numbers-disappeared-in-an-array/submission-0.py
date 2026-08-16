class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark numbers as seen by negating the value at their corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: If an index is still positive, its corresponding number (index + 1) is missing
        return [i + 1 for i, num in enumerate(nums) if num > 0]