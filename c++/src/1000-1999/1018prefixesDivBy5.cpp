#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int cur=0;
        int n = nums.size();
        vector<bool> ans(n, false);
        for (int i=0;i<n;i++) {
            cur=(cur<<1) + nums[i];
            cur%=5;
            ans[i]=cur==0;
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> tops{2,1,2,4,2,2}, bottom{5,2,6,2,3,2};
    Solution so;
    return 0;
}