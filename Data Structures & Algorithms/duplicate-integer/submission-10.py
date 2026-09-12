class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True # if a duplicate is found early, then it exits early
            seen.add(num)
        return False
        