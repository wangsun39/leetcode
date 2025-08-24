#include "lc_pub.h"

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int>l(n,0), r(n,0);
        int cnt=0;
        for (int i=1;i<n;i++) {
            if (nums[i-1]&&nums[i])
                l[i]=l[i-1]+1;
        }
        for (int i=n-2;i>=0;i--) {
            if (nums[i+1]&&nums[i])
                r[i]=r[i+1]+1;
        }
        int ans=0;
        for (int i=0;i<n;i++) {
            ans=max(ans,r[i]+l[i]);
        }
        return ans;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,0,1};

    Solution so;
    cout << so.longestSubarray(arr) << endl;
    return 0;
}
