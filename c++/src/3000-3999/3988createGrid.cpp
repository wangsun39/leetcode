// 给你三个整数 m、n 和 k。

// 构造一个大小为 m x n 的网格，该网格仅由字符 '.' 和 '#' 组成，其中：

// '.' 表示空单元格。
// '#' 表示障碍物单元格。
// 一条 有效路径 是满足以下条件的空单元格序列：

// 从左上角的单元格 (0, 0) 开始。
// 在右下角的单元格 (m - 1, n - 1) 结束。
// 只能：
// 向右移动，从 (i, j) 移动到 (i, j + 1)，或者
// 向下移动，从 (i, j) 移动到 (i + 1, j)。
// 返回 任意 一个网格，使得从左上角单元格到右下角单元格 恰好 有 k 条 有效路径。如果不存在这样的网格，则返回一个空数组。

 

// 示例 1：

// 输入： m = 2, n = 3, k = 2

// 输出： ["...","#.."]

// 解释：



// 从 (0, 0) 到 (1, 2) 恰好有 k = 2 条有效路径：

// (0, 0) → (0, 1) → (0, 2) → (1, 2)
// (0, 0) → (0, 1) → (1, 1) → (1, 2)
// 示例 2：

// 输入： m = 3, n = 3, k = 4

// 输出： ["..#","...","#.."]

// 解释：



// 从 (0, 0) 到 (2, 2) 恰好有 k = 4 条有效路径：

// (0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2)
// (0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
// (0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
// (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
// 示例 3：

// 输入： m = 1, n = 4, k = 2

// 输出： []

// 解释：​

// 对于 1 x 4 的网格，不存在恰好有 k = 2 条有效路径的网格，因此答案是一个空数组。

 

// 提示：

// 1 <= m, n <= 10
// 1 <= k <= 4

#include "lc_pub.h"

class Solution {
public:
    vector<string> createGrid(int m, int n, int k) {
        if (k==1) {
            for (int i=0;i<n;i++) {
                ans[0][i]='.';
            }
            for (int i=1;i<m;i++) {
                ans[i][n-1]='.';
            }
        }
        else if (k==2) {
            if (min(m,n)==1) return vector<string>{};
            ans[0][0]=ans[1][0]=ans[0][1]=ans[1][1]='.';
            for (int i=2;i<n;i++) {
                ans[1][i]='.';
            }
            for (int i=2;i<m;i++) {
                ans[i][n-1]='.';
            }
        }
        else if (k==3) {
            if (min(m,n)==1||max(m,n)<3) return vector<string>{};
            ans[0][0]=ans[1][0]=ans[0][1]=ans[1][1]='.';
            if (n==2) {
                ans[2][0]=ans[2][1]='.';
                for (int i=3;i<m;i++) {
                    ans[i][n-1]='.';
                }
            }
            else {
                ans[0][2]=ans[1][2]='.';
                for (int i=2;i<n;i++) {
                    ans[1][i]='.';
                }
                for (int i=2;i<m;i++) ans[i][n-1]='.';
            }
        }
        else {
            if (min(m,n)==1||max(m,n)<3) return vector<string>{};
            if (m==2&&n==3||m==3&&n==2) return vector<string>{};
            if (m==3&&n==3) {
                ans[0][0]=ans[1][0]=ans[0][1]=ans[1][1]=ans[1][2]=ans[2][1]=ans[2][2]='.';
            }
            else if (m<4){
                for (int i=0;i<4;i++) ans[0][i]='.';
                for (int i=0;i<n;i++) ans[1][i]='.';
                for (int i=2;i<m;i++) ans[i][n-1]='.';
            }
            else {
                for (int i=0;i<4;i++) ans[i][0]='.';
                for (int i=0;i<m;i++) ans[i][1]='.';
                for (int i=2;i<n;i++) ans[m-1][i]='.';
            }

        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
