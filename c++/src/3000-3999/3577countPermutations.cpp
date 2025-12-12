#include "lc_pub.h"


class Solution {
    public:
    int countPermutations(vector<int>& complexity) {
        int MOD=1e9+7;
        int n=complexity.size()-1;
        for (int i=1;i<n+1;i++) {
            if (complexity[0]>=complexity[i]) return 0;
        }
        long long ans=1;
        for (int i=2;i<=n;i++) {
            ans*=i;
            ans%=MOD;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{9,4,1,3,7};

    Solution so;
    cout<<so.countPermutations(nums, 4)<<endl;
    return 0;
}
