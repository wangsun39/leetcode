#include "lc_pub.h"

class Solution {
public:
    int concatenatedBinary(int n) {
        int MOD = 1e9+7;
        long long ans=0;
        for (int i=1;i<=n;i++) {
            int shift = __lg(i)+1;
            ans = ((ans << shift) + i) % MOD;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    return 0;
}
