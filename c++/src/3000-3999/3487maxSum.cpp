#include "lc_pub.h"


class Solution {
    public:
    int maxSum(vector<int>& nums) {
        unordered_set<int> s;
        int ans = 0;
        int zero = 0, neg = -INT_MAX;
        for (auto x: nums) {
            if (x > 0) {
                if (s.find(x) == s.end())
                    ans += x;
                s.emplace(x);
            }
            else if (x == 0) zero = 1;
            else {
                neg = max(neg, x);
            }
        }
        if (ans) return ans;
        if (zero) return 0;
        return neg;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    return 0;
}
