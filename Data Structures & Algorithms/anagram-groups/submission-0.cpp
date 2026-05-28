class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for(string s: strs){
            string key = s; //copies string
            sort(key.begin(), key.end()); // sorts characters
            groups[key].push_back(s); // groups by signature

        }

        vector<vector<string>> result;
        
        for(auto& pair : groups) {
            result.push_back(pair.second);
        }

        return result;
    }
};
