#include "lc_pub.h"

class Solution {
    public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long ans=0;
        int mx=ranges::max(nums);
        int r=-1, n=nums.size();
        int cnt=0;
        for (int l=0;l<n;l++) {
            while (r+1<n&&cnt<k) {
                r++;
                if (nums[r]==mx) cnt++;
                
            }
            if (cnt>=k) ans += n-r;
            if (nums[l]==mx) cnt--;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,2,3,3};

    Solution so;
    cout << so.countSubarrays(nums, 2) << endl;
    return 0;
}
