class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        if(nums[start]<nums[end]){
            return nums[start];
        }
        while(start<end){
            int mid = start + (end-start)/2;
            if(mid<end && nums[mid]>nums[mid+1]){
                return nums[mid+1];
            }
            if(mid>start && nums[mid-1]>nums[mid]){
                return nums[mid];
            }
            if(nums[mid]==nums[start] && nums[mid]==nums[end]){
                if(nums[start]>nums[start+1]){
                    return nums[start+1];
                }
                start++;
                if(nums[end-1]>nums[end]){
                    return nums[end];
                }
                end--;
            }
            else if(nums[start]<nums[mid]||(nums[start]==nums[mid]&&nums[mid]>nums[end])){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }
        return nums[start];
    }
}