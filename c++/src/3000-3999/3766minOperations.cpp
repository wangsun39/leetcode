
#include <stdio.h>
#include "lc_pub.h"

class Solution {
public:
    vector<int> minOperations(vector<int>& nums) {
        int n=nums.size();
        vector<int>ans(n,0);
        for (int i=0;i<n;i++) {
            int x=nums[i];
            int l=__lg(x)+1;
            int lh=l/2;
            int xh=x>>(l-lh);
            int mask=(1<<l)-1;
            int y=__builtin_bitreverse32(x)>>(32-l);
            int yh=y>>(l-lh);
            int xy=xh^yh;
            ans[i]=abs(xy-xh);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    return 0;
}
