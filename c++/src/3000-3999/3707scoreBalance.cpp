// 给你一个由小写英文字母组成的字符串 s。

// 一个字符串的 得分 是其字符在字母表中的位置之和，其中 'a' = 1，'b' = 2，...，'z' = 26。

// 请你判断是否存在一个下标 i，使得该字符串可以被拆分成两个 非空子字符串 s[0..i] 和 s[(i + 1)..(n - 1)]，且它们的得分 相等 。

// 如果存在这样的拆分，则返回 true，否则返回 false。

// 一个 子字符串 是字符串中 非空 的连续字符序列。

 

// 示例 1:

// 输入: s = "adcb"

// 输出: true

// 解释:

// 在下标 i = 1 处拆分：

// 左子字符串 = s[0..1] = "ad"，得分 = 1 + 4 = 5
// 右子字符串 = s[2..3] = "cb"，得分 = 3 + 2 = 5
// 两个子字符串的得分相等，因此输出为 true。

// 示例 2:

// 输入: s = "bace"

// 输出: false

// 解释:​​​​​​

// 没有拆分能产生相等的得分，因此输出为 false。

 

// 提示:

// 2 <= s.length <= 100
// s 由小写英文字母组成。

#include "lc_pub.h"

class Solution {
public:
    bool scoreBalance(string s) {
        vector<long long> nums;
        long long cur=0;
        for (char x:s) {
            nums.push_back(cur+=(x-'a'+1));
        }
        if (cur&1) return false;
        long long t=cur/2;
        auto p=ranges::lower_bound(nums,t);
        if (*p==t) return true;
        return false;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.scoreBalance("edb");
    return 0;
}
