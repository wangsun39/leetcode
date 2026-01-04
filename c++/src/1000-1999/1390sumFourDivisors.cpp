#include "lc_pub.h"

constexpr int MX = 100'001;
int divisor_num[MX];
int divisor_sum[MX];

auto init = [] {
    for (int i=1;i<MX;i++) {
        int j=i;
        while (j<MX) {
            divisor_num[j]++;
            divisor_sum[j]+=i;
            j+=i;
        }
    }
    return 0;
}();

class Solution {
    
    public:
    int sumFourDivisors(vector<int>& nums) {
        int ans=0;
        for (auto x: nums) {
            if (divisor_num[x]==4) {
                ans+=divisor_sum[x];
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
