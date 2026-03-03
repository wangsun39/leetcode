// 给你一个由小写英文字母组成的字符串 s。

// 你 必须 在字符串 s 中至少存在两个 连续 字符时，反复执行以下操作：

// 移除字符串中 最左边 的一对按照字母表 连续 的相邻字符（无论是按顺序还是逆序，例如 'a' 和 'b'，或 'b' 和 'a'）。
// 将剩余字符向左移动以填补空隙。
// 当无法再执行任何操作时，返回最终的字符串。

// 注意：字母表是循环的，因此 'a' 和 'z' 也视为连续。

 

// 示例 1：

// 输入: s = "abc"

// 输出: "c"

// 解释:

// 从字符串中移除 "ab"，剩下 "c"。
// 无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 "c"。
// 示例 2：

// 输入: s = "adcb"

// 输出: ""

// 解释:

// 从字符串中移除 "dc"，剩下 "ab"。
// 从字符串中移除 "ab"，剩下 ""。
// 无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 ""。
// 示例 3：

// 输入: s = "zadb"

// 输出: "db"

// 解释:

// 从字符串中移除 "za"，剩下 "db"。
// 无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 "db"。
 

// 提示:

// 1 <= s.length <= 105
// s 仅由小写英文字母组成。

#include "lc_pub.h"


class Solution {
    public:
    string resultingString(string s) {
        deque<char> dq;
        for (int x: s) {
            if (dq.size() && (abs(dq.back()-x)==1||abs(dq.back()-x)==25)) {
                dq.pop_back();
                continue;
            }
            dq.push_back(x);
        }
        string ans;
        for (char x: dq) {
            ans += x;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{7,2,0,4,2};

    Solution so;
    return 0;
}
