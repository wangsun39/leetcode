#include "lc_pub.h"


// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
    bool isPowerOfFour(int n) {
        return (n & (n - 1)) == 0 && (n & 0x55555555) == 0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
