#include "lc_pub.h"

class Solution {
    public:
    int longestSubarray(vector<int>& nums) {
        int mx = 0;
        int start = 0;
        int n=nums.size();
        int ans=0;
        for (int i=0;i<n;i++) {
            if (nums[i]<mx) {
                start=i+1;
                continue;
            }
            if (nums[i]>mx) {
                mx=nums[i];
                ans=1;
                start=i;
            }
            else {
                ans=max(ans,i-start+1);
                if (nums[i]!=nums[i-1]) start=i;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,2,3,3,2,2}, t{8,2,5,8};

    Solution so;
    cout << so.longestSubarray(arr) << endl;
    return 0;
}
