class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        aux(nums, target, left, right);
        return {left, right};
    }

    void aux(vector<int>& nums, int target, int& left, int& right) {
        if(left == right) return;

        int temp = right;
        while(temp > left) {
            if(nums[left] + nums[temp] == target) {
                right = temp;
                return;
            }
            temp--;
        }
        left++;
        aux(nums, target, left, right);
    }
};
