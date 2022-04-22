class Solution {
public:
    int numTrees(int n) {
        long long int sum = 1;

        for (int i = 2; i <= n; i++)
        {
            sum = sum * 2 * (2 * i - 1) / (i + 1) ;
        }
        return sum;
    }
};