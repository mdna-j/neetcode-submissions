class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set <int> seen; //initizlizes empty set

        for (int n: nums) { //next number in the array
            if (seen.count(n)) return true; //checks if the number exists in set
            seen.insert(n); //inserts number into seen set
        }
        return false;
    }
};