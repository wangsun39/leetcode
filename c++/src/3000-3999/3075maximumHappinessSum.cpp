#include "lc_pub.h"


class Solution {
    public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        ranges::sort(happiness, {}, [](auto x) {return -x;});
        long long ans = 0;
        for (int i=0;i<k;i++) {
            ans += max(happiness[i]-i,0);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
