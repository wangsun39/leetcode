#include "lc_pub.h"

class Solution {
    public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        int n=differences.size();
        vector<long long> nums(n+1);
        nums[0]=0;
        long long mx=0,mn=0;
        for (int i=0;i<n;i++) {
            nums[i+1]=nums[i]+differences[i];
            mx=max(mx, nums[i+1]);
            mn=min(mn, nums[i+1]);
        }
        return max((upper-lower)-(mx-mn) + 1, 0LL);
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{1,-3,4};

    Solution so;
    cout << so.numberOfArrays(arr,1,6) << endl;
    return 0;
}
