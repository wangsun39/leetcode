// 给你一个由小写英文字母组成的、长度为 n 的字符串 s。

// 你 必须执行 恰好 一次操作：选择一个整数 k，满足 1 <= k <= n，然后执行以下两个选项之一：

// 反转 s 的 前 k 个字符，或
// 反转 s 的 后 k 个字符。
// 返回在 恰好 执行一次此类操作后可以获得的 字典序最小 的字符串。

// 如果字符串 a 和字符串 b 在第一个不同的位置上，a 中的字母在字母表中比 b 中对应的字母出现得更早，则称字符串 a 字典序小于 字符串 b。如果前 min(a.length, b.length) 个字符都相同，则较短的字符串字典序较小。

 

// 示例 1:

// 输入: s = "dcab"

// 输出: "acdb"

// 解释:

// 选择 k = 3，反转前 3 个字符。
// 将 "dca" 反转为 "acd"，得到的字符串 s = "acdb"，这是可获得的字典序最小的字符串。
// 示例 2:

// 输入: s = "abba"

// 输出: "aabb"

// 解释:

// 选择 k = 3，反转后 3 个字符。
// 将 "bba" 反转为 "abb"，得到的字符串是 "aabb"，这是可获得的字典序最小的字符串。
// 示例 3:

// 输入: s = "zxy"

// 输出: "xzy"

// 解释:

// 选择 k = 2，反转前 2 个字符。
// 将 "zx" 反转为 "xz"，得到的字符串是 "xzy"，这是可获得的字典序最小的字符串。
 

// 提示:

// 1 <= n == s.length <= 1000
// s 由小写英文字母组成。

#include "lc_pub.h"

class Solution {
public:
    string lexSmallest(string s) {
        int n=s.size();
        string ans=s;
        for (int i=1;i<n;i++) {
            string s1=s.substr(0, i);
            ranges::reverse(s1);
            ans=min(ans,s1+s.substr(i));
            s1=s.substr(n-i);
            ranges::reverse(s1);
            ans=min(ans,s.substr(0,n-i)+s1);
        }
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
