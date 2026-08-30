// 给你一个整数数组 nums。

// 对于 nums 中的每个整数 x，首先生成一个由 x 个小写字母 'a' 组成的字符串。

// 你可以执行以下操作任意次（包括零次）：

// 选择两个 相邻且相同 的字母，并将它们替换为字母表中的下一个字母。
// 例如，"aa" 可以替换为 "b"，"bb" 可以替换为 "c"。对 "zz" 则无法进行替换。

// 对于每个 x，请你确定可以获得的 字典序最大 的字符串。

// 返回一个字符串数组，其中第 i 个字符串是 nums[i] 的答案。

// 在两个字符串不同处的第一个位置，如果字符串 a 包含的字母在字母表中的顺序晚于 b 中的相应字母，则字符串 a 字典序大于 字符串 b。如果前 min(a.length, b.length) 个字符相同，则较长的字符串字典序更大。

 

// 示例 1：

// 输入： nums = [2,5,7]

// 输出： ["b","ca","cba"]

// 解释：

// nums[0] = 2："aa" → "b"。
// nums[1] = 5："aaaaa" → "baaa" → "bba" → "ca"。
// nums[2] = 7："aaaaaaa" → "baaaaa" → "bbaaa" → "bbba" → "cba"。
// 因此，ans = ["b", "ca", "cba"]。
// 示例 2：

// 输入： nums = [3,9,1]

// 输出： ["ba","da","a"]

// 解释：

// nums[0] = 3："aaa" → "ba"。
// nums[1] = 9："aaaaaaaaa" → "baaaaaaa" → "bbaaaaa" → "bbbaaa" → "bbbba" → "cbba" → "cca" → "da"。
// nums[2] = 1：无法进行任何转换，因此结果为 "a"。
// 因此，ans = ["ba", "da", "a"]。
 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 108

#include "lc_pub.h"

class Solution {
public:
    vector<string> largestString(vector<int>& nums) {
        vector<char> alpha(26);
        for (int i=0;i<26;i++) alpha[i]='a'+i;
        int n=nums.size();
        vector<string> ans(n);
        for (int i=0;i<n;i++) {
            int j=nums[i];
            while (j > 0) {
                int log_=log2(j);
                log_=min(log_,25);
                char t='a' + log_;
                auto p=ranges::lower_bound(alpha, t);
                j-=1<<log_;
                ans[i]+='a'+log_;
            }
        }

        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{67108864,9,7};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.largestString(nums);
    return 0;
}
