#include "lc_pub.h"

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n<=0) return false;
        return __builtin_popcount(n) == 1;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    vector<int> nums = {3,2,1,5,6,4};
    auto v = so.isPowerOfTwo(2);
    cout << v << endl;
    return 0;
}
