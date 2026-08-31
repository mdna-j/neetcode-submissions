class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array of distinct integers, that is sorted in ascending order, and an integer target
        left, right = 0, len(nums) - 1
        # function must find for target within nums
        while left <= right:
            mid = (left + right) // 2

        #if it exists return its index
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # otherwise return -1
        return -1


        