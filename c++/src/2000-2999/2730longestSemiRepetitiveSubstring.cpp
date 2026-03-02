// 给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。

// 如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，"0010" 、"002020" 、"0123" 、"2002" 和 "54944" 是半重复字符串，而 "00101022" （相邻的相同数字对是 00 和 22）和 "1101234883" （相邻的相同数字对是 11 和 88）不是半重复字符串。

// 请你返回 s 中最长 半重复 子字符串 的长度。

 

// 示例 1：

// 输入：s = "52233"

// 输出：4

// 解释：

// 最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。

// 示例 2：

// 输入：s = "5494"

// 输出：4

// 解释：

// s 是一个半重复字符串。

// 示例 3：

// 输入：s = "1111111"

// 输出：2

// 解释：

// 最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。

 

// 提示：

// 1 <= s.length <= 50
// '0' <= s[i] <= '9'

#include "lc_pub.h"

class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int n=s.size();
        vector<int>p(1,0);
        int ans = 0;
        for (int i=1;i<n;i++) {
            if (s[i]==s[i-1]) {
                p.push_back(i);
            }
        }
        p.push_back(n);
        if (p.size()<=2) return n;
        for (int i=2;i<p.size();i++) {
            ans=max(ans,p[i]-p[i-2]);
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
