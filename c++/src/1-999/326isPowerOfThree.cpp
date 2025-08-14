#include "lc_pub.h"

class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    vector<int> nums = {1,2147483647};
    auto v = so.isPowerOfThree(27);
    cout << v << endl;
    return 0;
}
