class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k%nums.size();
        vector<int> ans;
        int pivot = nums.size()-k;
        for(int i=pivot;i<nums.size();i++){
            ans.push_back(nums[i]);
        }
        for(int i=0;i<pivot;i++){
            ans.push_back(nums[i]);
        }
        nums = ans;
    }
};