#include "lc_pub.h"


class Solution {
    public:
    int countValidSelections(vector<int>& nums) {
        int s=0,n=nums.size();
        for (int i=0;i<n;i++) s+=nums[i];
        int ans=0;
        int cur=0;
        for (int i=0;i<n;i++) {
            cur+=nums[i];
            if (cur * 2 > s) return ans;
            if (nums[i]==0&&cur * 2 == s) ans+=2;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,0,2,0,3};

    Solution so;
    cout<<so.countValidSelections(nums)<<endl;
    return 0;
}
