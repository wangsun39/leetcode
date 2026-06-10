// 给你一个整数 n 。

// 如果其二进制表示中 恰好 仅包含 一对 连续的置位 ，则返回 true ，否则返回 false 。

// 整数中的 置位 是指其 二进制 表示中的 1 。
 

// 示例 1：

// 输入： nums = 6

// 输出： true

// 解释：

// 6 的二进制表示为 110 。
// 恰好存在一对连续的置位（"11"）。因此，答案为 true 。
// 示例 2：

// 输入： nums = 5

// 输出： false

// 解释：

// 5 的二进制表示为 101 。
// 不存在连续的置位。因此，答案为 false 。
 

// 提示：

// 0 <= n <= 105

#include "lc_pub.h"

class Solution {
public:
    bool consecutiveSetBits(int n) {
        int c=0;
        int p=n%2;
        n/=2;
        while (n) {
            if (p==1&&n%2==1) c++;
            p=n%2;
            n/=2;
        }
        return c==1;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{73,92,31,78,89};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
