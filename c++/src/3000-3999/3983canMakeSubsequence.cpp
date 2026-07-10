// 给你两个由小写英文字母组成的字符串 s 和 t。

// 你最多可以选择 s 中的一个下标，并将该下标处的字符 替换 为任意小写英文字母。

// 如果可以使 s 成为 t 的一个 子序列，则返回 true；否则返回 false。

// 子序列 是指通过删除另一个字符串中的某些字符或不删除任何字符，并且不改变剩余字符相对顺序后得到的字符串。

 

// 示例 1：

// 输入： s = "cat", t = "chat"

// 输出： true

// 解释：

// 将 s[1] 从 'a' 替换为 'h'，得到字符串 "cht"。
// "cht" 是 "chat" 的子序列，因为可以按顺序匹配 'c'、'h' 和 't'。
// 示例 2：

// 输入： s = "plane", t = "apple"

// 输出： false

// 解释：

// 字符 'p'、'l' 和 'e' 可以在 t 中匹配，但其余字符无法在保持所需顺序的前提下匹配。
// 即使替换 s 中的任意一个字符，也无法使 s 成为 t 的子序列。
 

// 提示：

// 1 <= s.length, t.length <= 105
// s 和 t 仅由小写英文字母组成。

#include "lc_pub.h"

class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int ns=s.size(),nt=t.size();
        vector<int>left(nt, 0),right(nt,0);  // t的左右两侧对s的最大覆盖长度
        int p=0;
        if (t[0]==s[0]) {
            left[0]=1;
            p=1;
        }
        for (int i=1;i<nt;i++) {
            if (p>=ns) {
                left[i]=left[i-1];
                continue;
            }
            if (t[i]==s[p]) {
                p++;
                left[i]=left[i-1]+1;
            }
            else {
                left[i]=left[i-1];
            }
        }
        p=ns-1;
        if (t[nt-1]==s[p]) {
            right[nt-1]=1;
            p--;
        }
        for (int i=nt-2;i>=0;i--) {
            if (p<0) {
                right[i]=right[i+1];
                continue;
            }
            if (t[i]==s[p]) {
                p--;
                right[i]=right[i+1]+1;
            }
            else {
                right[i]=right[i+1];
            }
        }
        for (int i=0;i<nt;i++) {
            int l=0,r=0;
            if (i>0) l=left[i-1];
            if (i<nt-1) r=right[i+1];
            if (l+r>=ns-1) return true;
        }
        return false;
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
