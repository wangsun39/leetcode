// 给你一个仅由字符 'a'、'b' 和 'c' 组成的字符串 s。

// 如果一个字符串不包含 "abc" 作为 子序列 ，那么它被称为 有效的 。

// 返回 s 中 有效子串 的数量。起始或结束下标不同的子串分别计数。

// 子串 是字符串内连续的 非空 字符序列。

// 子序列 是指从另一个字符串中删除一些或不删除字符，且不改变剩余字符顺序所得到的新字符串。

 

// 示例 1：

// 输入： s = "abac"

// 输出： 9

// 解释：

// 以下子串不包含 "abc" 作为子序列：

// s[0..0] = "a"
// s[0..1] = "ab"
// s[0..2] = "aba"
// s[1..1] = "b"
// s[1..2] = "ba"
// s[1..3] = "bac"
// s[2..2] = "a"
// s[2..3] = "ac"
// s[3..3] = "c"
// 因此，答案是 9。

// 示例 2：

// 输入： s = "abc"

// 输出： 5

// 解释：

// 以下子串不包含 "abc" 作为子序列：

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

// s 中的所有子串都不包含 "abc"​​​​​​​ 作为子序列。因此，答案是 3。

 

// 提示：

// 1 <= s.length <= 105​​​​​​​
// s 仅由字符 'a'、'b' 和 'c' 组成。



#include "lc_pub.h"

class Solution {
public:
    long long countValidSubstrings(string s) {
        int n=s.size();
        int pa=-1,pb=-1;  // 记录窗口内最后一组 a, b的位置
        int pa2=-1;  // 记录窗口内最后一个 a 的位置
        int l=0;
        long long ans=0;
        for (int r=0;r<n;r++) {
            if (s[r]=='a') {
                pa2=r;
            }
            else if (s[r]=='b') {
                if (pa2!=-1) {
                    pa=pa2;
                    pb=r;
                }
            }
            else {
                while (pa!=-1) {
                    if (s[l]=='a') {
                        if (pa==l) {
                            pa=pb=-1;
                            if (pa2==l)
                                pa2=-1;
                        }
                    }
                    l++;
                }
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
