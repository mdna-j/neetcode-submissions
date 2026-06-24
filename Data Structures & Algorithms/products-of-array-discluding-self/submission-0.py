class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # Initialize the output array with 1s
        result = [1] * length
        
        # Step 1: Calculate prefix products (left to right)
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate postfix products and combine (right to left)
        postfix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result