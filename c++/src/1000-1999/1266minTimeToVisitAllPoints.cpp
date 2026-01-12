#include "lc_pub.h"

class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int dp0[3]={0,INT_MIN,INT_MIN};
        int dp1[3]={0};
        for (int x: nums) {
            if (x%3==0) {
                dp1[0]=max(dp0[0],dp0[0]+x);
                dp1[1]=max(dp0[1],dp0[1]+x);
                dp1[2]=max(dp0[2],dp0[2]+x);
            }
            else if(x%3==1) {
                dp1[0]=max(dp0[0],dp0[2]+x);
                dp1[1]=max(dp0[1],dp0[0]+x);
                dp1[2]=max(dp0[2],dp0[1]+x);
            }
            else {
                dp1[0]=max(dp0[0],dp0[1]+x);
                dp1[1]=max(dp0[1],dp0[2]+x);
                dp1[2]=max(dp0[2],dp0[0]+x);
            }
            memcpy(dp0,dp1,sizeof(dp0));
        }
        return dp0[0];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,6,5,1,8};
    Solution so;
    cout << so.maxSumDivThree(nums) <<endl;
    return 0;
}