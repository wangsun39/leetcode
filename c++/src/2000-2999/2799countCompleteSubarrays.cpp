#include "lc_pub.h"

class Solution {
    public:
    int countCompleteSubarrays(vector<int>& nums) {
        int m = unordered_set(nums.begin(), nums.end()).size();
        unordered_map<int, int> counter;
        int n = nums.size();
        int r=-1,ans=0;
        for (int l=0;l<n;l++) {
            while (r+1<n&&counter.size()<m) {
                r++;
                counter[nums[r]]++;
            }
            if (counter.size() < m) break;
            ans += (n - r);
            if (--counter[nums[l]] == 0) counter.erase(nums[l]);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,1,2,2};

    Solution so;
    cout << so.countCompleteSubarrays(nums) << endl;
    return 0;
}
