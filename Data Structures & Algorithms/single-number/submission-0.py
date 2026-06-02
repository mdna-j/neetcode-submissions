class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num # XOR accummulates, the pairs are removed
        return ans

        