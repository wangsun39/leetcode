// 给你一个二维整数数组 towers，其中 towers[i] = [xi, yi, qi] 表示第 i 座塔的坐标 (xi, yi) 和质量因子 qi。

// 另外给你一个整数数组 center = [cx, cy] 表示你的位置，以及一个整数 radius。

// 如果一座塔与 center 之间的 曼哈顿距离小于或等于 radius，则称该塔是 可到达的。

// 在所有可到达的塔中：

// 返回质量因子 最大 的塔的坐标。
// 如果存在并列的塔，返回坐标 字典序最小 的塔。如果没有塔是可到达的，返回 [-1, -1]。
// 两点 (xi, yi) 和 (xj, yj) 之间的 曼哈顿距离 为 |xi - xj| + |yi - yj|。
// 坐标 [xi, yi] 字典序小于 [xj, yj] 是指：xi < xj，或者 xi == xj 且 yi < yj。

// |x| 表示 x 的 绝对值。

 

// 示例 1：

// 输入： towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2

// 输出： [3,1]

// 解释：

// 塔 [1, 2, 5]：曼哈顿距离 = |1 - 1| + |2 - 1| = 1，可到达。
// 塔 [2, 1, 7]：曼哈顿距离 = |2 - 1| + |1 - 1| = 1，可到达。
// 塔 [3, 1, 9]：曼哈顿距离 = |3 - 1| + |1 - 1| = 2，可到达。
// 所有塔都是可到达的。最大质量因子为 9，对应塔 [3, 1]。

// 示例 2：

// 输入： towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5

// 输出： [1,3]

// 解释：

// 塔 [1, 3, 4]：曼哈顿距离 = |1 - 0| + |3 - 0| = 4，可到达。
// 塔 [2, 2, 4]：曼哈顿距离 = |2 - 0| + |2 - 0| = 4，可到达。
// 塔 [4, 4, 7]：曼哈顿距离 = |4 - 0| + |4 - 0| = 8，不可到达。
// 在可到达的塔中，最大质量因子为 4。[1, 3] 和 [2, 2] 的质量因子相同，因此返回字典序较小的坐标 [1, 3]。

// 示例 3：

// 输入： towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1

// 输出： [-1,-1]

// 解释：

// 塔 [5, 6, 8]：曼哈顿距离 = |5 - 1| + |6 - 2| = 8，不可到达。
// 塔 [0, 3, 5]：曼哈顿距离 = |0 - 1| + |3 - 2| = 2，不可到达。
// 在给定半径内没有可到达的塔，故返回 [-1, -1]。

 

// 提示：

// 1 <= towers.length <= 105
// towers[i] = [xi, yi, qi]
// center = [cx, cy]
// 0 <= xi, yi, qi, cx, cy <= 105
// 0 <= radius <= 105

#include "lc_pub.h"

class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {
        int mn=-1;
        vector<int>ans;
        for (auto &tower: towers) {
            if (abs(tower[0]-center[0])+abs(tower[1]-center[1])<=radius&&(tower[2]>mn||(tower[2]==mn&&tower<ans))) {
                mn=tower[2];
                ans={tower[0], tower[1]};
            }
        }
        if (mn==-1) return {-1,-1};
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    return 0;
}
