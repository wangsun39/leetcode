// 给你一个仅由字符 'a'、'b' 和 'c' 组成的字符串 s。

// 如果一个字符串不包含 "abc" 作为 子串 ，那么它被称为 有效的 。

// 返回 s 中 有效子串 的数量。起始或结束下标不同的子串分别计数。

// 子串 是字符串内连续的 非空 字符序列。

 

// 示例 1：

// 输入： s = "abac"

// 输出： 10

// 解释：

// 以下子串不包含 "abc" 作为子串：

// s[0..0] = "a"
// s[0..1] = "ab"
// s[0..2] = "aba"
// s[0..3] = "abac"
// s[1..1] = "b"
// s[1..2] = "ba"
// s[1..3] = "bac"
// s[2..2] = "a"
// s[2..3] = "ac"
// s[3..3] = "c"
// 因此，答案是 10。

// 示例 2：

// 输入： s = "abc"

// 输出： 5

// 解释：

// 以下子串不包含 "abc"​​​​​​​ 作为子串：

// s[0..0] = "a"
// s[0..1] = "ab"
// s[1..1] = "b"
// s[1..2] = "bc"
// s[2..2] = "c"​​​​​​​
// 因此，答案是 5。

// 示例 3：

// 输入： s = "ac"

// 输出： 3

// 解释：

// s 中的所有子串都不包含 "abc" 作为子串​​​​​​​。因此，答案是 3。

 

// 提示：

// 1 <= s.length <= 105​​​​​​​
// s 仅由字符 'a'、'b' 和 'c' 组成。



#include "lc_pub.h"

class Solution {
public:
    long long countValidSubstrings(string s) {
        int n=s.size();
        int l=0;
        long long ans=0;
        for (int r=0;r<n;r++) {
            if (r>1&&s[r]=='c'&&s[r-1]=='b'&&s[r-2]=='a') {
                l=r-1;
            }
            ans+=r-l+1;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{4,2,3,1},locked={0,1,1,0};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.countValidSubstrings("abcbc")<<endl;

    return 0;
}
