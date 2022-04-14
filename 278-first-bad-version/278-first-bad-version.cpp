// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 0,right = n,pivot = n/2;
        while(left<=right){
            pivot = left + (right-left)/2;
            if (isBadVersion(pivot)){
                right = pivot - 1;
            }
            else{
                left = pivot + 1;
            }
        }
        return left;
    }
};