#include "lc_pub.h"


class Solution {
    public:
    int specialTriplets(vector<int>& nums) {
        unordered_map<int, long long>left, right;
        int MOD=1e9+7;
        int n=nums.size();
        for (int i=2;i<n;i++) {
            right[nums[i]]++;
        }
        left[nums[0]]++;
        long long ans=0;
        for (int i=1;i<n-1;i++) {
            ans+=left[nums[i]*2]*right[nums[i]*2];
            ans%=MOD;
            left[nums[i]]++;
            right[nums[i+1]]--;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{9,4,1,3,7};

    Solution so;
    return 0;
}
