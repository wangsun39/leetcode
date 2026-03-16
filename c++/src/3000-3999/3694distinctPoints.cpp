// 给你一个由字符 'U'、'D'、'L' 和 'R' 组成的字符串 s，表示在无限的二维笛卡尔网格上的移动。

// 'U': 从 (x, y) 移动到 (x, y + 1)。
// 'D': 从 (x, y) 移动到 (x, y - 1)。
// 'L': 从 (x, y) 移动到 (x - 1, y)。
// 'R': 从 (x, y) 移动到 (x + 1, y)。
// 你还得到了一个正整数 k。

// 你 必须 选择并移除 恰好一个 长度为 k 的连续子字符串 s。然后，从坐标 (0, 0) 开始，按顺序执行剩余的移动。

// 返回可到达的 不同 最终坐标的数量。

 

// 示例 1:

// 输入：s = "LUL", k = 1

// 输出：2

// 解释：

// 移除长度为 1 的子字符串后，s 可以是 "UL"、"LL" 或 "LU"。执行这些移动后，最终坐标将分别是 (-1, 1)、(-2, 0) 和 (-1, 1)。有两个不同的点 (-1, 1) 和 (-2, 0)，因此答案是 2。

// 示例 2:

// 输入：s = "UDLR", k = 4

// 输出：1

// 解释：

// 移除长度为 4 的子字符串后，s 只能是空字符串。最终坐标将是 (0, 0)。只有一个不同的点 (0, 0)，因此答案是 1。

// 示例 3:

// 输入：s = "UU", k = 1

// 输出：1

// 解释：

// 移除长度为 1 的子字符串后，s 变为 "U"，它总是以 (0, 1) 结束，因此只有一个不同的最终坐标。

 

// 提示:

// 1 <= s.length <= 105
// s 只包含 'U'、'D'、'L' 和 'R'。
// 1 <= k <= s.length

#include "lc_pub.h"

class Solution {
    public:
    int distinctPoints(string s, int k) {
        vector<vector<int>> pos;
        pos.push_back({0,0});
        int n = s.size();
        for (int i=0;i<n;i++) {
            int u, v;
            if (s[i] == 'U') {
                u=pos[i][0];
                v=pos[i][1]+1;
            }
            else if (s[i] == 'D') {
                u=pos[i][0];
                v=pos[i][1]-1;
            }
            else if (s[i] == 'R') {
                u=pos[i][0]+1;
                v=pos[i][1];
            }
            else {
                u=pos[i][0]-1;
                v=pos[i][1];
            }
            pos.push_back({u, v});
        }
        unordered_set<long long> us;
        int x=pos[n][0],y=pos[n][1];
        for (int i=k;i<=n;i++) {
            int dx=pos[i][0]-pos[i-k][0], dy=pos[i][1]-pos[i-k][1];
            us.insert((long long)(x-dx)*1000000+(y-dy));
        }
        return us.size();
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{10,4,3,6,4,5,6,1,4};

    Solution so;
    cout<<so.distinctPoints("UD", 1)<<endl;
    return 0;
}
