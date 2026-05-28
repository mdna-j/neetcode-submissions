class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> processed;

        for(int num: nums){
            if(processed.count(num)){
                return true;

            }
            processed.insert(num);
        }
        return false;
    }
};