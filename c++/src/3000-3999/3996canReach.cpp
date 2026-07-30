// 给你两个整数数组 start 和 target，每个数组的形式均为 [x, y]，表示标准 8 x 8 国际象棋棋盘上的一个格子。

// 如果骑士可以用 偶数 次移动从 start 到达 target，则返回 true；否则返回 false。

// 注意：骑士的一次合法移动是：沿一个方向移动两格，再沿与其垂直的方向移动一格。下图展示了骑士从一个格子出发时所有 8 种可能的移动方式。



 

// 示例 1：

// 输入： start = [1,1], target = [2,2]

// 输出： true

// 解释：

// 一种可行的移动序列为 (1, 1) -> (3, 2) -> (2, 4) -> (4, 3) -> (2, 2)。

// 骑士经过 4 次移动到达目标位置，4 是偶数。因此答案为 true。

// 示例 2：

// 输入： start = [4,5], target = [6,6]

// 输出： false

// 解释：

// 骑士无法用偶数次移动从 start = [4, 5] 到达 target = [6, 6]。因此答案为 false。

 

// 提示：

// start.length == target.length == 2
// 0 <= start[i], target[i] <= 7

#include "lc_pub.h"

class Solution {
public:
    bool canReach(vector<int>& start, vector<int>& target) {
        if (start == target) return true;
        vector<vector<int>> f(8, vector<int>(8, 0));
        deque<vector<int>> dq;
        dq.push_back({start[0], start[1], 0});
        f[start[0]][start[1]] = 1;
        vector<pair<int,int>> dir{{-1,-2},{-2,-1},{1,2},{2,1},{1,-2},{-2,1},{-1,2},{2,-1}};
        while (dq.size()) {
            int x=dq[0][0],y=dq[0][1],t=dq[0][2];
            dq.pop_front();
            for (auto &[dx, dy]: dir) {
                int u=x+dx,v=y+dy;
                if (u<8&&u>=0&&v<8&&v>=0&&f[u][v]==0) {
                    if (u==target[0]&&v==target[1]) {
                        if (t&1) return true;
                        return false;
                    }
                    dq.push_back({u, v,1-t});
                    f[u][v]=1;
                }
            }
        }
        return false;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> strs{"0?1"};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
