// 给你一个二进制字符串 s。

// 另给定一个字符串数组 strs，其中每个 strs[i] 的长度都与 s 相同，并且仅由字符 '0'、'1' 和 '?' 组成。每个 '?' 都可以替换为 '0' 或 '1'。

// 你可以执行以下操作任意次（也可以不执行）：

// 选择 s 的任意一个 子序列 sub。
// 将 sub 按 非递减 顺序排序。
// 用排序后的 sub 替换 s 中被选中的 子序列，其余字符保持不变。
// 返回一个布尔数组 ans。如果可以将 strs[i] 中的所有 '?' 替换为 '0' 或 '1'，并使用上述操作将 s 转换为替换后的字符串，则 ans[i] 为 true；否则为 false。

// 子序列 是指通过删除一个序列中的某些元素或不删除任何元素，并且不改变剩余元素相对顺序后得到的序列。

 

// 示例 1：

// 输入： s = "101", strs = ["1?1","0?1","0?0"]

// 输出： [true,true,false]

// 解释：

// i	strs[i]	替换方式	替换后的 strs[i]	操作	结果
// 0	"1?1"	? → 0	"101"	与 s 相同。	true
// 1	"0?1"	? → 1	"011"	选择 s 中下标为 [0..2] 的子序列，得到 "101"。
// 将 "101" 排序后得到 "011" = strs[i]。	true
// 2	"0?0"	? → 0 或 1	"000" 或 "010"	无法实现。	false
// 因此，ans = [true, true, false]。

// 示例 2：

// 输入： s = "1100", strs = ["0011","11?1","1?1?"]

// 输出： [true,false,true]

// 解释：

// i	strs[i]	替换方式	替换后的 strs[i]	操作	结果
// 0	"0011"	-	"0011"	选择 s 中下标为 [0..3] 的子序列，得到 "1100"。
// 将 "1100" 排序后得到 "0011" = strs[i]。	true
// 1	"11?1"	? → 0	"1101"	无法实现。	false
// 2	"1?1?"	第一个 ? → 0
// 第二个 ? → 0	"1010"	选择 s 中下标为 [1, 2] 的子序列，得到 "10"。
// 将 "10" 排序后得到 "01"，因此 s = "1010"。	true
// 因此，ans = [true, false, true]。

// 示例 3：

// 输入： s = "1010", strs = ["0011"]

// 输出： [true]

// 解释：

// i	strs[i]	替换方式	替换后的 strs[i]	操作	结果
// 0	"0011"	-	"0011"	选择 s 中下标为 [0, 2, 3] 的子序列，得到 "110"。
// 将 "110" 排序后得到 "011"，因此 s = "0011" = strs[i]。	true
// 因此，ans = [true]。

 

// 提示：

// 1 <= n == s.length <= 2000
// s[i] 为 '0' 或 '1'。
// 1 <= strs.length <= 2000
// strs[i].length == n
// strs[i] 仅由 '0'、'1' 和 '?' 组成。

#include "lc_pub.h"

class Solution {
public:
    vector<bool> transformStr(string s, vector<string>& strs) {
        int n=s.size(),m=strs.size();
        vector<bool> ans(m, false);
        auto calc = [&](this auto && check, string &t) -> bool {
            int c0=0,c1=0;  // ? 对应的0的个数和1的个数
            int d0=0,d1=0;  // s[i]与t[i]不等时 s[i]对应的0的个数和1的个数
            vector<int> idx;  // 记录不相等的下标
            for (int i=0;i<n;i++) {
                if (s[i]==t[i]) continue;
                idx.push_back(i);
                if (t[i]=='?') {
                    if (s[i]=='0') c0++;
                    else c1++;
                }
                else {
                    if (s[i]=='0') d0++;
                    else {
                        if (d0) return false;
                        d1++;
                    }
                }
            }
            if (d0>d1) {
                return d0-d1<=c1;
            }
            return d1-d0<=c0;
        };
        for (int i=0;i<m;i++) {
            ans[i]=calc(strs[i]);
        }
        return ans;
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
