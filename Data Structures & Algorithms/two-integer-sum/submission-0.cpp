class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen; // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // If we've already seen the complement
            if (seen.count(complement)) {
                return {seen[complement], i};
            }

            // Store current value with its index
            seen[nums[i]] = i;
        }

        return {}; // guaranteed one solution exists
    }
};
