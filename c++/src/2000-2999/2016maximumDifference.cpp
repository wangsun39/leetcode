#include "lc_pub.h"

class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int mn=nums[0];
        int n = nums.size();
        int ans=-1;
        for (int i=1;i<n;i++) {
            if (nums[i]>mn)
                ans=max(ans,nums[i]-mn);
            else mn=min(mn,nums[i]);
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {7,1,5,4};

    Solution so;
    cout << so.maximumDifference(arr) << endl;
    return 0;
}
