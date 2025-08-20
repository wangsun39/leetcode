#include "lc_pub.h"

class Solution {
    public:
    long long zeroFilledSubarray(vector<int>& nums) {
        int l = -1,n=nums.size();
        long long ans=0;
        for (long long r=0;r<n;r++) {
            if (nums[r] == 0) {
                ans += r - l;
            }
            else {
                l = r;
            }
        }
        return ans;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.zeroFilledSubarray(arr) << endl;
    return 0;
}
