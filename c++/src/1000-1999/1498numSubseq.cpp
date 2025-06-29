#include "lc_pub.h"

#define MX  100'000
#define MOD  1'000'000'007

long long pow2[MX+1];
auto init = [] {
    pow2[0]=1;
    for (int i=1;i<=MX;i++) {
        pow2[i]=(pow2[i-1]*2)%MOD;
    }
    return 0;
}();

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        ranges::sort(nums);
        int l=0,n=nums.size();
        long long ans=0;
        for (int r=0;r<n;r++) {
            if (nums[0]+nums[r]>target) break;
            if (l==r&&nums[r]*2<=target) {
                ans+=pow2[r];
                ans%=MOD;
                l++;
                continue;
            }

            while (nums[r]+nums[l]>target) l--;
            ans += (pow2[l+1]-1)*(pow2[r-l-1]);
            
            ans %= MOD;
        }
        return ans;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {2,3,3,4,6,7};

    Solution so;
    cout << so.numSubseq(arr, 12) << endl;
    return 0;
}
