#include "lc_pub.h"


class Solution {
    public:
    int maxDistinctElements(vector<int>& nums, int k) {
        ranges::sort(nums);
        int ans=1,pre=nums[0]-k,n=nums.size();
        for (int i=1;i<n;i++) {
            if (pre+1>nums[i]+k) continue;
            if (nums[i]-k<=pre+1) {
                pre++;
            }
            else {
                pre=nums[i]-k;
            }
            ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    cout << so.maxDistinctElements(nums,2) << endl;
    return 0;
}
