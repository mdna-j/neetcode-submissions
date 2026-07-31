class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num_to_next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                num_to_next_greater[stack.pop()] = num
            stack.append(num)
            
        return [num_to_next_greater.get(num, -1) for num in nums1]
