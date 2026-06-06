class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicate values for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the current number is greater than 0, the sum can never be 0
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1  # Sum is too small, increase it
                elif current_sum > 0:
                    right -= 1  # Sum is too large, decrease it
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
