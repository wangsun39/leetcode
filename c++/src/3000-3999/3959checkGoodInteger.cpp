// 给你一个正整数 n。

// 令 digitSum 表示 n 的各位数字之和，令 squareSum 表示 n 的各位数字平方之和。

// 如果一个整数满足 squareSum - digitSum >= 50，则称它是 好整数 。

// 如果 n 是好整数，返回 true；否则，返回 false。

 

// 示例 1：

// 输入： n = 1000

// 输出： false

// 解释：

// 1000 的数字为 1、0、0 和 0。
// digitSum 为 1 + 0 + 0 + 0 = 1。
// squareSum 为 12 + 02 + 02 + 02 = 1。
// squareSum - digitSum 为 1 - 1 = 0。由于 0 小于 50，因此输出 false。
// 示例 2：

// 输入： n = 19

// 输出： true

// 解释：

// 19 的数字为 1 和 9。
// digitSum 为 1 + 9 = 10。
// squareSum 为 12 + 92 = 1 + 81 = 82。
// squareSum - digitSum 为 82 - 10 = 72。由于 72 大于等于 50，因此输出 true。
 

// 提示：

// 1 <= n <= 109

#include "lc_pub.h"

class Solution {
public:
    bool checkGoodInteger(int n) {
        int a=0,b=0;
        while (n) {
            int x=n%10;
            a+=x;
            b+=x*x;
            n/=10;
        }
        return a+50<=b;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,2,1,2,3,3,3};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
