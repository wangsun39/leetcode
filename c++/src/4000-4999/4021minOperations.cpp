// 给你一个由小写英文字母组成的字符串 s 。

// 你可以按任意顺序执行以下操作任意次（包括零次）：

// 递增：选择任意一个下标 i 并将 s[i] 替换为下一个小写英文字母。'z' 之后的字母是 'a' 。
// 左旋：将字符串的第一个字符移动到末尾。
// 返回使 s 成为 回文串 所需的 最少 操作次数。

// 回文串 是正着读和反着读都一样的字符串。

 

// 示例 1：

// 输入： s = "abc"

// 输出： 2

// 解释：

// 一种最优方案：
// 左旋字符串："abc" -> "bca" 。
// 递增 'a' 为 'b'："bca" -> "bcb" 。
// "bcb" 是一个回文串。因此，答案是 2 。
// 示例 2：

// 输入： s = "yb"

// 输出： 3

// 解释：

// 将第一个字符递增三次："yb" -> "zb" -> "ab" -> "bb" 。
// "bb" 是一个回文串。因此，答案是 3 。
 

// 提示：

// 2 <= s.length <= 2000
// s 仅由小写英文字母组成。

#include "lc_pub.h"

class Solution {
public:
    int minOperations(string s) {
        int n=s.size();
        int ans=n*25;
        auto diff=[&](char a,char b) -> int {
            return min(abs(a-b), 26-abs(a-b));
        };
        for (int i=0;i<n;i++) {
            // 回文串从s[i]开始
            int cnt=i;
            for (int j=0;j<n/2;j++) {
                char a=s[(i+j)%n];
                char b=s[(i-j-1+n)%n];
                cnt+=diff(a,b);
            }
            ans=min(ans,cnt);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{5,2,3,1,4,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.minOperations("xyz");
    return 0;
}
