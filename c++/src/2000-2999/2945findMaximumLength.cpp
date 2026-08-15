// 给你一个下标从 0 开始的整数数组 nums 。

// 你可以执行任意次操作。每次操作中，你需要选择一个 子数组 ，并将这个子数组用它所包含元素的 和 替换。比方说，给定数组是 [1,3,5,6] ，你可以选择子数组 [3,5] ，用子数组的和 8 替换掉子数组，然后数组会变为 [1,8,6] 。

// 请你返回执行任意次操作以后，可以得到的 最长非递减 数组的长度。

// 子数组 指的是一个数组中一段连续 非空 的元素序列。

 

// 示例 1：

// 输入：nums = [5,2,2]
// 输出：1
// 解释：这个长度为 3 的数组不是非递减的。
// 我们有 2 种方案使数组长度为 2 。
// 第一种，选择子数组 [2,2] ，对数组执行操作后得到 [5,4] 。
// 第二种，选择子数组 [5,2] ，对数组执行操作后得到 [7,2] 。
// 这两种方案中，数组最后都不是 非递减 的，所以不是可行的答案。
// 如果我们选择子数组 [5,2,2] ，并将它替换为 [9] ，数组变成非递减的。
// 所以答案为 1 。
// 示例 2：

// 输入：nums = [1,2,3,4]
// 输出：4
// 解释：数组已经是非递减的。所以答案为 4 。
// 示例 3：

// 输入：nums = [4,3,2,6]
// 输出：3
// 解释：将 [3,2] 替换为 [5] ，得到数组 [4,5,6] ，它是非递减的。
// 最大可能的答案为 3 。
 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 105

#include "lc_pub.h"

class Solution {
    public:
    int findMaximumLength(vector<int>& nums) {
        int n=nums.size();
        vector<long long> dp(n, 0), last(n, 0), s(n, 0);
        // dp[i]  前i个数合并后的最长长度，last[i] 在合并前i个数，达到最长长度下，合并后的最后一个元素最小可能值
        dp[0]=1;s[0]=last[0]=nums[0];
        deque<pair<long long, int>> dq;
        dq.push_back({s[0]+last[0],0});  // 单调队列维护 {s[j]+last[j], j}，单调 s[j]+last[j] 递增
        int p = -1;   // dq中最后一个s[j]+last[j]<=s[i]的位置
        // 在单调队列中，p位置及p位置左侧的元素都是满足 s[j]+last[j]<=s[i] 即 s[i]-s[j]>=last[j], 即区间 [j+1,i] 和能作为合并后的最后一项
        // f[i] 是单调上升的，因此单调队列 dq 中p位置是能达到最大可能f[i]的位置，同时s[j]也是单调上升的，因此 dq[p]也是能达到最小last[i]的位置
        // 为了保证dq的单调性，dq后侧是可以弹出元素的，因为如果 s[j]+last[j] >= s[i]+last[i] 其中 s[j]<s[i],f[j]<=f[i] => last[j]>last[i] 这样的j没有必要被后面的元素选中
        // 可以直接扔掉

        for (int i=1;i<n;i++) {
            s[i]=s[i-1]+nums[i];
            while (p + 1 < dq.size()) {
                if (dq[p+1].first<=s[i]) p++;
                else break;
            }
            if (p == -1) {
                last[i]=last[i-1]+nums[i];
                dp[i]=dp[i-1];
                dq.push_back({s[i]+last[i], i});
                continue;
            }
            int t=dq[p].second;  // 原数组中上一段的结束下标
            last[i]=s[i]-s[t];
            dp[i]=dp[t]+1;
            long long v=s[i]+last[i];
            // 将v放入dq
            while (dq.size()) {
                auto &end=dq.back();
                if (end.first<v)
                    break;
                dq.pop_back();
                
            }
            if (dq.size()<=p) {
                    p=dq.size()-1;
                }
            dq.push_back({v, i});
        }

        return dp[n-1];
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{417,241,895,308,259,562};

    Solution so;
    cout<<so.findMaximumLength(nums)<<endl;
    return 0;
}
