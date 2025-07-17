#include "lc_pub.h"


class Solution {
    public:
    int maximumLength(vector<int>& nums) {
        int dp0=0,dp1=0;
        int n=nums.size();
        int odd;
        if (nums[0]&1) {dp1=1;odd=1;}
        else dp0=1;
        for (int i=1;i<n;i++) {
            if (nums[i]&1) {
                dp1=dp0+1;
                odd++;
            }
            else {
                dp0=dp1+1;
            }
        }
        int ans=max(odd,n-odd);
        return max(ans, max(dp0,dp1));
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4};

    Solution so;
    cout << so.maximumLength(nums) << endl;
    return 0;
}
