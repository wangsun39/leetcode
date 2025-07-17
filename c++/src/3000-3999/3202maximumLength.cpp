#include "lc_pub.h"


class Solution {
    public:
    int maximumLength(vector<int>& nums, int k) {
        int n=nums.size();
        for (int i=0;i<n;i++) nums[i]%=k;
        int ans=0;
        for (int i=0;i<k;i++) {
            vector<int> counter(k, 0);  // 结尾是模为k的最长长度
            for (int j=0;j<n;j++) {
                int t=(i+k-nums[j])%k;
                counter[nums[j]]=counter[t]+1;
                ans=max(ans,counter[nums[j]]);
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5};

    Solution so;
    cout << so.maximumLength(nums,2) << endl;
    return 0;
}
