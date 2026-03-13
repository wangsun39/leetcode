// 给你一个 n × m 的网格和一个整数 k。

// 一个放置在单元格 (r, c) 的传感器可以覆盖所有与 (r, c) 的 切比雪夫距离不超过 k 的单元格。

// 两个单元格 (r1, c1) 和 (r2, c2) 之间的 切比雪夫距离 为 max(|r1 − r2|,|c1 − c2|)。

// 你的任务是返回覆盖整个网格所需传感器的 最少 数量。

 

// 示例 1:

// 输入: n = 5, m = 5, k = 1

// 输出: 4

// 解释:

// 在位置 (0, 3)、(1, 0)、(3, 3) 和 (4, 1) 放置传感器可以确保网格中的每个单元格都被覆盖。因此，答案是 4。

// 示例 2:

// 输入: n = 2, m = 2, k = 2

// 输出: 1

// 解释:

// 当 k = 2 时，无论传感器放在哪个位置，单个传感器都可以覆盖整个 2 * 2 的网格。因此，答案是 1。

 

// 提示:

// 1 <= n <= 103
// 1 <= m <= 103
// 0 <= k <= 103

#include "lc_pub.h"


class Solution {
    public:
    int minSensors(int n, int m, int k) {
        int x = k * 2 + 1;
        return ((n + x - 1) / x) * ((m + x - 1) / x);
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    return 0;
}
