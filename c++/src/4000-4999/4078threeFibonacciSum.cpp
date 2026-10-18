// 给你一个整数 n。

// 斐波那契数列 以 0 和 1 开始，之后的每个数都是前两个数之和。它的前几项为 0, 1, 1, 2, 3, 5, 8, 13, ...。

// 如果 n 可以表示为斐波那契数列中 连续三项之和，则返回 true；否则返回 false。

 

// 示例 1：

// 输入： n = 16

// 输出： true

// 解释：

// 连续三项 3、5 和 8 的和为 3 + 5 + 8 = 16。

// 示例 2：

// 输入： n = 8

// 输出： false

// 解释：

// 虽然 1 + 2 + 5 = 8，但这三项在斐波那契数列中并不连续。不存在连续三项的和等于 8。

// 示例 3：

// 输入： n = 2

// 输出： true

// 解释：

// 斐波那契数列的前三项之和为 0 + 1 + 1 = 2。

 

// 提示：

// 1 <= n <= 109

#include "lc_pub.h"

#define MX 45
int f[MX];
vector<int>s(MX, 0);

auto init = [] {
    f[0]=0;
    f[1]=1;
    for (int i=2;i<MX;i++) {
        f[i]=f[i-1]+f[i-2];
        s[i]=f[i-1]+f[i-2]+f[i];
    }
    return 0;
}();

class Solution {
public:
    bool threeFibonacciSum(int n) {
        auto it=lower_bound(s.begin(), s.end(), n);
        return *it==n;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
