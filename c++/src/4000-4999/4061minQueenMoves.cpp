// 一个 8 x 8 的空棋盘，其行和列的下标从 1 开始。

// 给你一个数组 source = [sr, sc] 表示 皇后 的初始位置，以及一个数组 target = [tr, tc] 表示目标位置。

// 在一步移动中，皇后可以在棋盘范围内，沿着单条 行 、 列 或 对角线 移动一个或多个方格。

// 返回皇后移动到 恰好 落在 target 位置所需的 最小 移动次数。

 

// 示例 1：

// 输入： source = [8,1], target = [1,8]

// 输出： 1

// 解释：



// 单次对角线移动即可让皇后直接从 (8, 1) 移动到 (1, 8)。

// 示例 2：

// 输入： source = [4,2], target = [1,3]

// 输出： 2

// 解释：

// ​​​​​​​

// 皇后先从 (4, 2) 移动到 (4, 3)，然后从 (4, 3) 移动到 (1, 3)，共用 2 步移动到达目标位置。

// 示例 3：

// 输入： source = [1,1], target = [1,1]

// 输出： 0

// 解释：

// 皇后已经处于目标位置，因此不需要任何移动。

 

// 提示：​​​​​​​

// source == [sr, sc]
// target == [tr, tc]
// 1 <= sr, sc, tr, tc <= 8

#include "lc_pub.h"

class Solution {
public:
    int minQueenMoves(vector<int>& source, vector<int>& target) {
        if (source==target) return 0;
        if (source[0]==target[0]||source[1]==target[1]) {
            return 1;
        }
        if (abs(source[0]-target[0])==abs(source[1]-target[1])) {
            return 1;
        }
        return 2;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-10,-21,-7};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
