// 给你两个字符串 source 和 target。

// 同时给你一个二维字符串数组 rules，其中 rules[i] = [patterni, replacementi]，以及一个整数数组 costs，其中 costs[i] 是应用 rules[i] 的基本成本。两个数组长度相同。此外，patterni 和 replacementi 的长度也相同。

// 你可以 任意 次数地应用 任意 规则。每次应用规则 rule[i] 的过程如下：

// 选择当前字符串的一个下标 l，使得从 l 到 l + patterni.length - 1 的位置范围存在于当前字符串中，并且这些位置中 没有 任何一个在之前的规则应用中被使用过。
// 对于 patterni 每个下标 j，字符 patterni[j] 必须 等于 当前字符串位置 l + j 处的字符，或者是 '*'。
// 将该范围内的字符替换为 replacementi。替换内容将 完全 按照给定的使用，且不包含通配符。
// 这次规则应用的成本是 costs[i] 加上 patterni 中 '*' 字符的数量。
// 一旦某个字符位置在某次规则应用中被使用，它就 不能 在 后续 的任何规则应用中被再次使用。
// 因为每个 patterni 和 replacementi 的长度都相同，所以在每次规则应用之后，字符的位置都会保留。

// 返回将 source 转换为 target 所需的 最小 总成本。如果无法完成转换，则返回 -1。

 

// 示例 1：

// 输入： source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]

// 输出： 7

// 解释：

// 应用 rules[0]，将 "he" 替换为 "wo"，成本为 3，字符串变为 "wollo"。
// 应用 rules[1]，将 "llo" 替换为 "rld"，成本为 4，字符串变为 "world"。
// 总成本为 3 + 4 = 7。
// 示例 2：

// 输入： source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2]

// 输出： 3

// 解释：

// 应用 rules[0] 将 "cat" 替换为 "dog"。通配符 '*' 匹配 'a'，在基本成本 2 的基础上增加 1。
// 总成本为 2 + 1 = 3。
// 示例 3：

// 输入： source = "test", target = "next", rules = [["*e*t","next"]], costs = [4]

// 输出： 6

// 解释：

// 应用 rules[0] 将 "test" 替换为 "next"。第一个通配符匹配 't'，第二个通配符匹配 's'，在基本成本 4 的基础上增加 2。
// 总成本为 4 + 2 = 6。
// 示例 4：

// 输入： source = "ab", target = "bc", rules = [["a*","bd"]], costs = [9]

// 输出： -1

// 解释：

// 没有任何规则应用序列可以将 source 转换为 target，因此答案是 -1。

 

// 提示：

// 1 <= source.length, target.length <= 5000
// source 和 target 仅由小写英文字母组成。
// 1 <= rules.length == costs.length <= 200
// rules[i] = [patterni, replacementi]
// 1 <= patterni.length == replacementi.length <= 20
// patterni 至少包含一个小写英文字母，且最多包含 5 个 '*' 字符。
// replacementi 仅包含小写英文字母。
// 1 <= costs[i] <= 1000

#include "lc_pub.h"

class Solution {
public:
    int minCost(string source, string target, vector<vector<string>>& rules, vector<int>& costs) {
        int n=source.size(),m=rules.size();
        for (int i=0;i<m;i++) {
            costs[i]+=ranges::count(rules[i][0], '*');
        }
        auto check1 = [&](this auto && check, int rule_i, int src_i) -> bool {
            for (int i=0;i<rules[rule_i][0].size();i++) {
                if (rules[rule_i][0][i]=='*'||rules[rule_i][0][i]==source[src_i+i]) continue;
                return false;
            }
            return true;
        };
        auto check2 = [&](this auto && check, int rule_i, int dst_i) -> bool {
            for (int i=0;i<rules[rule_i][1].size();i++) {
                if (rules[rule_i][1][i]==target[dst_i+i]) continue;
                return false;
            }
            return true;
        };
        vector<int>dp(n,INT_MAX);  // 前i个字符的转换的最小代价
        for (int i=0;i<n;i++) {
            if (source[i] == target[i]) {
                if (i == 0) dp[0] = 0;
                else if (dp[i - 1] < INT_MAX) {
                    dp[i] = dp[i-1];
                }
            }
            for (int j=0;j<m;j++) {
                int k=rules[j][0].size();
                if (k>i+1) continue;
                if (!check1(j,i-k+1)||!check2(j,i-k+1)) continue;
                if (k==i+1) {
                    dp[i]=min(dp[i],costs[j]);
                }
                else {
                    if (dp[i-k]<INT_MAX) {
                        dp[i]=min(dp[i],dp[i-k]+costs[j]);
                    }
                }
            }
        }
        if (dp[n-1]==INT_MAX) return -1;
        return dp[n-1];
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,2,4,5,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    // cout<<so.minAdjacentSwaps(nums, 3,4);
    return 0;
}
