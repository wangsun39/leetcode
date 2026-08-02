// 给你两个非负整数 n 和 s。

// 返回满足下述条件的 最大 整数：

// 最多有 n 位数字。
// 其各位数字之和等于 s 。
// 如果不存在这样的整数，则返回 -1。

 

// 示例 1：

// 输入： n = 2, s = 9

// 输出： 90

// 解释：

// 最多由 2 位数字组成且各位数字之和为 9 的最大整数是 90。

// 示例 2：

// 输入： n = 2, s = 19

// 输出： -1

// 解释：

// 不存在最多由 2 位数字组成且各位数字之和为 19 的整数，因此答案为 -1。

// 示例 3：

// 输入： n = 5, s = 0

// 输出： 0

// 解释：

// 唯一一个各位数字之和为 0 的非负整数是 0。

 

// 提示：

// 1 <= n <= 5
// 0 <= s <= 100

#include "lc_pub.h"

class Solution {
public:
    int largestInteger(int n, int s) {
        if (9 * n < s) return -1;
        int ans=0;
        for (int i=n-1;i>=0;i--) {
            int t=min(s,9);
            ans+=pow(10,i)*t;
            s-=t;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> strs{"?1?"};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
