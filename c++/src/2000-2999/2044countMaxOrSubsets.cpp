#include "lc_pub.h"

class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int s = 0;
        for (auto x: nums) s|=x;
        int n=nums.size(),ans=0;
        for (int x=1;x<1<<n;x++) {
            int v=0;
            for (int i=0;i<n;i++) {
                if ((1<<i)&x) v|=nums[i];
            }
            if (v==s) ans++;
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {3,1};

    Solution so;
    cout << so.countMaxOrSubsets(arr) << endl;
    return 0;
}
