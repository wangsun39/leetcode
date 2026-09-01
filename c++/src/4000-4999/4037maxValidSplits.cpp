// 给你一个整数数组 nums。

// 你可以从 nums 中移除 至多一个 元素。记 arr 为按原始顺序保留其余元素后得到的数组，m 为其长度。

// 如果 arr 的 分割位置 i 满足以下条件，则称其为 有效的 ：

// 0 <= i < m - 1，且
// gcd(arr[0..i]) == gcd(arr[i + 1..m - 1])。
// 长度为 1 的数组没有有效的分割位置。

// arr 的 得分 是有效分割位置的数量。

// 返回 arr 的 最大可能得分 。

// gcd(a) 表示数组 a 中所有元素的最大公约数。

 

// 示例 1：

// 输入： nums = [10,30,15,10]

// 输出： 2

// 解释：

// 一种最优解是移除 nums[2] = 15。此时 arr = [10, 30, 10]。

// 分割位置如下：

// 分割位置 i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
// 0	10	10
// 1	10	10
// 所有分割位置都是有效的。因此，答案为 2。

// 示例 2：

// 输入： nums = [2,10,14]

// 输出： 1

// 解释：

// 一种最优解是不移除任何元素。此时 arr = [2, 10, 14]。

// 分割位置如下：

// 分割位置 i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
// 0	2	2
// 1	2	14
// 只有下标 0 处的分割位置是有效的。因此，答案为 1。

// 示例 3：

// 输入： nums = [2,4]

// 输出： 0

// 解释：

// 唯一拥有分割位置的剩余数组是 arr = [2, 4]。

// 分割位置如下：

// 分割位置 i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
// 0	2	4
// 没有有效的分割位置。因此，答案为 0。

 

// 提示：

// 2 <= nums.length <= 105
// 1 <= nums[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    int maxValidSplits(vector<int>& nums) {
        unordered_set<int> pos;  // 导致前后缀gcd变化的位置，其他位置不必考虑，即使删除得分也不会变
        int n=nums.size();
        vector<int> g1(n,0);
        g1[0]=nums[0];
        for (int i=1;i<n;i++) {
            g1[i]=gcd(g1[i-1], nums[i]);
            if (g1[i]<g1[i-1]) {
                pos.insert(i);
            }
        }
        vector<int> g2(n,0);
        g2[n-1]=nums[n-1];
        for (int i=n-2;i>=0;i--) {
            g2[i]=gcd(g2[i+1], nums[i]);
            if (g2[i]<g2[i+1]) {
                pos.insert(i);
            }
        }
        int ans=0;
        for (int i=0;i<n-1;i++) {
            if (g1[i]==g2[i+1])
                ans++;
        }

        auto calc = [&](int idx) -> int {
            vector<int> g1(n-1,0),g2(n-1,0);
            int a=idx!=0?0:1,b=idx!=n-1?n-1:n-2;
            g1[0]=nums[a];
            int p=1;
            for (int i=a+1;i<n;i++) {
                if (i==idx) continue;
                g1[p]=gcd(g1[p-1], nums[i]);
                p++;
            }
            g2[n-2]=nums[b];
            p=n-3;
            for (int i=b-1;i>=0;i--) {
                if (i==idx) continue;
                g2[p]=gcd(g2[p+1], nums[i]);
                p--;
            }
            int res=0;
            for (int i=0;i<n-2;i++) {
                if (g1[i]==g2[i+1])
                    res++;
            }
            return res;
        };

        for (int i: pos) {
            ans=max(ans, calc(i));
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{9,5,10};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maxValidSplits(nums);
    return 0;
}
