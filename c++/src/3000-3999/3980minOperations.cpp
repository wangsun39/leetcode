// 给你两个长度同为 n 的二进制字符串 s1 和 s2 。

// 你可以对 s1 以任意顺序执行以下操作 任意 次：

// 选择一个满足 s1[i] 为 '0' 的下标 i ，并将其更改为 '1' 。
// 选择一个满足 0 <= i < n - 1 且 s1[i] 和 s1[i + 1] 均为 '1' 的下标 i 。将这两个字符都更改为 '0' 。
// 返回使 s1 等于 s2 所需的 最小 操作次数。如果无法使 s1 等于 s2 ，则返回 -1 。

 

// 示例 1：

// 输入： s1 = "11", s2 = "00"

// 输出： 1

// 解释：

// 在一次操作中将下标 0 和 1 从 '1' 更改为 '0' ，这样 "11" 就变成了 "00" 。因此，答案为 1 。

// 示例 2：

// 输入： s1 = "01", s2 = "10"

// 输出： 3

// 解释：

// 将下标 0 从 '0' 更改为 '1' ，这样 "01" 就变成了 "11" 。
// 将下标 0 和 1 从 '1' 更改为 '0' ，这样 "11" 就变成了 "00" 。
// 将下标 0 从 '0' 更改为 '1' ，这样 "00" 就变成了 "10" 。
// 因此，答案为 3 。
// 示例 3：

// 输入： s1 = "1", s2 = "0"

// 输出： -1

// 解释：

// 第一个操作不能将 '1' 更改为 '0' ，而第二个操作需要两个相邻的字符。因此，这是不可能的。

 

// 提示：

// 1 <= n == s1.length == s2.length <= 105
// s1 和 s2 仅由 '0' 和 '1' 组成。

#include "lc_pub.h"

unordered_map<string, int> mp{{"1010", 0},{"1000",2},{"1011",1},{"1001",3},
                              {"0010", 1},{"0000",0},{"0011",2},{"0001",1},
                              {"1110", 2},{"1100",1},{"1111",0},{"1101",2},
                              {"0110", 3},{"0100",2},{"0111",1},{"0101",0}};
class Solution {
public:
    int minOperations(string s1, string s2) {
        int n=s1.size();
        vector<int> dp(n, INT_MAX), dp1(n, INT_MAX);  // 将前i个字母变成与s2相同操作次数dp[i], 将前i-1个字母变成与s2相同第i个字母变成相反的操作次数dp1[i]
        if (s1[0]==s2[0]) dp[0] = 0;
        else if (s1[0]=='0'&&s2[0]=='1') dp[0] = 1;

        for (int i=1;i<n;i++) {
            if (s1[i]==s2[i]) dp[i]=dp[i-1];
            else if (s1[i]=='0'&&s2[i]=='1'&&dp[i-1]<INT_MAX) dp[i] = dp[i-1]+1;
            if (i>1) {
                if (dp[i-2]<INT_MAX) {
                    dp[i]=min(dp[i],dp[i-2]+mp[s1.substr(i-1,2)+s2.substr(i-1,2)]);

                    string dst{s2[i-1]};
                    if (s2[i]=='0')dst+='1';
                    else dst+='0';
                    dp1[i]=min(dp1[i],dp[i-2]+mp[s1.substr(i-1,2)+dst]);
                }
                if (dp1[i-1]<INT_MAX) {
                    string src;
                    if (s2[i-1]=='0')src+='1';
                    else src+='0';
                    src+=s1[i];
                    dp[i]=min(dp[i],dp1[i-1]+mp[src+s2.substr(i-1,2)]);
                }
            }
            else {
                dp[i]=min(dp[i],mp[s1.substr(i-1,2)+s2.substr(i-1,2)]);
                string dst{s2[i-1]};
                if (s2[i]=='0')dst+='1';
                else dst+='0';
                dp1[i]=min(dp1[i],mp[s1.substr(i-1,2)+dst]);
            }
        }
        if (dp[n-1]==INT_MAX) return -1;
        return dp[n-1];
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.minOperations("101","000");
    return 0;
}
