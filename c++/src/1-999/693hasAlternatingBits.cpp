#include "lc_pub.h"

class Solution {
public:
    bool hasAlternatingBits(int n) {
        int m = __lg(n)+1;
        long long mask = (1LL << m) - 1;
        long long v1 = 0x55555555 & mask, v2 = 0xaaaaaaaa & mask;
        return (n ^ v1) == 0 || (n ^ v2) == 0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    return 0;
}