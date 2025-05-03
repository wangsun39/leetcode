#include "lc_pub.h"


class Solution {
    public:
    long long countSubarrays(vector<int>& nums, long long k) {
        int n = nums.size();
        long long ans = 0, s=0;
        int r = -1;
        for (int l=0;l<n;l++) {
            while (r + 1 < n && (s + (long long)nums[r + 1]) * (r - l + 2) < k) {
                r++;
                s += nums[r];
            }
            if (r < l) {
                r++;
                continue;
            }
            ans += (r - l + 1);
            s -= nums[l];
        }
        return ans;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7};

    Solution so;
    cout << so.countSubarrays(arr, 4) << endl;
    return 0;
}
