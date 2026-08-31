// 给你一个 8 x 8 的棋盘，行和列的下标从 1 开始。

// 给你一个数组 source = [sr, sc]，表示 象 的起始位置，以及一个数组 target = [tr, tc]。在一步移动中，象可以在棋盘范围内沿着单个 对角线 方向移动任意数量的格子。

// 返回象 恰好 到达 target 位置所需的 最少 移动次数。如果它永远无法到达 target，则返回 -1。

 

// 示例 1：

// 输入： source = [8,1], target = [1,8]

// 输出： 1

// 解释：



// 一步对角线移动即可将象直接从 (8, 1) 送达 (1, 8)。

// 示例 2：

// 输入： source = [4,2], target = [1,3]

// 输出： 2

// 解释：



// 象从 (4, 2) 移动到 (3, 1)，然后再从 (3, 1) 移动到 (1, 3)，经过 2 步移动到达目标位置。

// 示例 3：

// 输入： source = [1,1], target = [3,4]

// 输出： -1

// 解释：

// 无论进行多少次对角线移动，从 (1, 1) 出发的象都永远无法到达 (3, 4)。因此，答案是 -1。

 

// 提示：

// source.length == target.length == 2
// 1 <= sr, sc, tr, tc <= 8
// source != target

#include "lc_pub.h"

static constexpr int DIRS[4][2] = {{1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

class Solution {
public:
    int minBishopMoves(vector<int>& source, vector<int>& target) {
        int sx=source[0],sy=source[1];
        int tx=target[0],ty=target[1];
        if ((sx+sy)%2!=(tx+ty)%2) return -1;
        if (source == target) return 0;
        if (sx-tx==sy-ty || sx-tx==-(sy-ty))
            return 1;
        vector<vector<int>> adj;
        for (auto& [dx, dy] : DIRS) {
            int l=1;
            while (true) {
                int x = sx + dx*l, y = sy + dy*l; // 相邻格子
                if (1 <= x && x <= 8 && 1 <= y && y <= 8) {
                    if (x-tx==y-ty || x-tx==-(y-ty)) return 2;
                }
                else {
                    break;
                }
                l++;
            }
        }
        return 3;  // 实际走不到这里
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
