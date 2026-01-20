#include "lc_pub.h"

class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n=nums.size();
        vector<int>ans(n, 0);
        for (int i=0;i<n;i++) {
            int x=nums[i];
            if (x==2) {
                ans[i]=-1;
                continue;
            }
            int j=0;
            while (x & (1 << j)) {
                j++;
            }
            ans[i]=x^(1<<(j-1));
        }
        return ans;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {0,1,0,1};

    Solution so;
    return 0;
}
