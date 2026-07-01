class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an array of numbers
        seen = set()
        #return true if value appears more than once
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        # else return false
        return False