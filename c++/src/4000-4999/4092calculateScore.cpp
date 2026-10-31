// 给你两个整数 a 和 b。

// 设 s1 和 s2 分别为 a 和 b 的二进制表示中置位的数量。

// 这两个整数的得分定义如下：

// 如果 s1 >= s2，则得分为 s1 * s2。
// 否则，得分为 s2 / s1，其中除法采用整数除法。
// 返回一个整数，表示 a 和 b 的得分。

// 置位是指数的二进制表示中值为 1 的位。

 

// 示例 1：

// 输入： a = 14, b = 6

// 输出： 6

// 解释：

// a = 14 的二进制表示为 "1110"，因此 s1 = 3。
// b = 6 的二进制表示为 "110"，因此 s2 = 2。
// 由于 s1 > s2，a 和 b 的得分为 s1 * s2 = 3 * 2 = 6。
// 示例 2：

// 输入： a = 5, b = 15

// 输出： 2

// 解释：

// a = 5 的二进制表示为 "101"，因此 s1 = 2。
// b = 15 的二进制表示为 "1111"，因此 s2 = 4。
// 由于 s1 < s2，a 和 b 的得分为 s2 / s1 = 4 / 2 = 2。
// 示例 3：

// 输入： a = 10, b = 12

// 输出： 4

// 解释：

// a = 10 的二进制表示为 "1010"，因此 s1 = 2。
// b = 12 的二进制表示为 "1100"，因此 s2 = 2。
// 由于 s1 == s2，a 和 b 的得分为 s1 * s2 = 2 * 2 = 4。
 

// 提示：

// 1 <= a, b <= 100


#include "lc_pub.h"

class Solution {
public:
    int calculateScore(int a, int b) {
        int na=__builtin_popcount(a);
        int nb=__builtin_popcount(b);
        if (na>=nb) return na*nb;
        return nb/na;
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
