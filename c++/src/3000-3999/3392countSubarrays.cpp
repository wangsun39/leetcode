#include "lc_pub.h"


class Solution {
    public:
    int countSubarrays(vector<int>& nums) {
        int ans = 0,n=nums.size();
        for (int i=1;i<n-1;i++){
            if (nums[i] == (nums[i-1]+nums[i+1])*2) ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,1,4,1};

    Solution so;
    cout << so.countSubarrays(nums) << endl;
    return 0;
}
