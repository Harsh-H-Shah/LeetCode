class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if( k == 0 ) return;
        int N = nums.size(), displaced = 0;
        for(int i=0; displaced<N; ++i){
            int tmp = nums[i];
            for(int x=1; ((i+x*k)%N)!=i; ++x,++displaced)
                swap(tmp, nums[(i+x*k)%N]);
            nums[i] = tmp;
            ++displaced;
        }
    }
};