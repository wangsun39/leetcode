// 给你一个 m x n 的矩阵 grid，其中每个单元格包含以下字符之一：

// 'L'：向左移动一格。
// 'R'：向右移动一格。
// 'U'：向上移动一格。
// 'D'：向下移动一格。
// 你从单元格 (0, 0) 出发，并将其视为已访问。每一步都按照当前单元格中的字符指示，移动到对应的单元格。

// 如果下一步移动会离开网格，或者进入一个已经访问过的单元格，则移动过程 结束 。在这两种情况下，该次移动都 不会 执行。

// 返回一个整数数组 [r, c]，表示 最后一个访问的单元格 的 行下标和列下标 。下标从 0 开始。

 

// 示例 1：

// 输入： grid = [["R","D"],["U","L"]]

// 输出： [1,0]

// 解释：

// 从单元格 (0, 0) 出发，其中的字符为 'R'，因此向右移动到 (0, 1)。
// 在单元格 (0, 1) 中，字符为 'D'，因此向下移动到 (1, 1)。
// 在单元格 (1, 1) 中，字符为 'L'，因此向左移动到 (1, 0)。
// 在单元格 (1, 0) 中，字符为 'U'，表示应移动到 (0, 0)。但 (0, 0) 已经访问过，因此不会执行该次移动。
// 因此，移动过程结束于最后访问的单元格 (1, 0)，答案为 [1, 0]。
// 示例 2：

// 输入： grid = [["R","R","R"]]

// 输出： [0,2]

// 解释：

// 从单元格 (0, 0) 出发，其中的字符为 'R'，因此向右移动到 (0, 1)。
// 在单元格 (0, 1) 中，字符为 'R'，因此向右移动到 (0, 2)。
// 在单元格 (0, 2) 中，字符为 'R'，表示应移动到 (0, 3)。但 (0, 3) 位于网格之外，因此不会执行该次移动。
// 因此，移动过程结束于最后访问的单元格 (0, 2)，答案为 [0, 2]。
 

// 提示：

// 1 <= m == grid.length <= 105
// 1 <= n == grid[i].length <= 105
// m * n <= 105
// grid[i][j] 为 'L'、'R'、'U' 或 'D' 之一。


#include "lc_pub.h"

class Solution {
public:
    vector<int> lastVisitedCell(vector<vector<char>>& grid) {
        int r=grid.size(),c=grid[0].size();
        int x=0,y=0;
        unordered_set<long long>vis;
        vis.insert(0);
        vector<int> ans(2,0);
        while (1) {
            if (grid[x][y]=='L') {
                y--;
            }
            else if (grid[x][y]=='R') {
                y++;
            }
            else if (grid[x][y]=='U') {
                x--;
            }
            else {
                x++;
            }
            if (x<0||x>=r||y<0||y>=c) {
                break;
            }
            // cout<<x<<y<<endl;
            long long key=(((long long)x)<<32)+y;
            if (vis.find(key)!=vis.end()) {
                break;
            }
            ans[0]=x;
            ans[1]=y;
            vis.insert(key);
        }
        return ans;
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
