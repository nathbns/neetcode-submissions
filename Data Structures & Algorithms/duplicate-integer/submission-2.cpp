class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> hm = {};
        for(int num: nums) {
            hm[num]++;
            if(hm[num] > 1) return true;
        }
        return false;
    }
};