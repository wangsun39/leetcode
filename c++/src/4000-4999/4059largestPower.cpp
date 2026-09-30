// 给你一个长度为 n 的整数数组 nums。你可以重新排列其中的元素以形成任意 排列 perm。

// 定义一个长度为 15 的数组 power。对于每个 0 <= i < 15，考查 perm 的前 j 个元素的第 (14 - i) 位，power[i] 是满足这些位全为 1 的最大整数 j（其中 0 <= j <= n）。

// 二进制位的位置从右向左编号，从第 0 位开始。

// 返回可能得到的 字典序最大 的 power 数组。

// 排列 是数组中所有元素的一种重新排列。

// 置位 指的是数字在二进制表示中对应位的值为 1。

// 对于两个长度相同的数组，如果在它们不同的第一个下标处，数组 a 包含的元素大于数组 b 中的元素，则称数组 a 的 字典序大于 数组 b。

 

// 示例 1：

// 输入：nums = [7,5]

// 输出：[0,0,0,0,0,0,0,0,0,0,0,0,2,1,2]

// 解释：

// 选择 perm = [7, 5]。

// 两个元素的第 2 位都置位了，因此 power[12] = 2。
// 第一个元素的第 1 位置位了，但第二个元素没有，因此 power[13] = 1。
// 两个元素的第 0 位都置位了，因此 power[14] = 2。
// 第一个元素的所有更高位都未置位，因此其余项都为 0。

// 示例 2：

// 输入：nums = [3,1,7]

// 输出：[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3]

// 解释：

// 选择 perm = [7, 3, 1]。

// 第一个元素的第 2 位置位了，但第二个元素没有，因此 power[12] = 1。
// 前两个元素的第 1 位都置位了，但第三个元素没有，因此 power[13] = 2。
// 所有三个元素的第 0 位都置位了，因此 power[14] = 3。
// 第一个元素的所有更高位都未置位，因此其余项都为 0。

 

// 提示：

// 1 <= nums.length <= 5 * 104
// 0 <= nums[i] < 215

#include "lc_pub.h"

class Solution {
public:
    vector<int> largestPower(vector<int>& nums) {
        int mask=(1<<15)-1;
        int n=nums.size();
        int start=0;
        while (start<n-1) {
            int mx=0;
            for (int i=start;i<n;i++) {
                mx=max(mx, nums[i]);
            }
            mask&=mx;  // start 之后的数，如果mask位以外的数位非0，是没有意义的，可以直接去掉，再比较大小
            for (int i=start;i<n;i++) {
                nums[i]&=mask;
                if (nums[i]==mask) {
                    swap(nums[i], nums[start]);
                    start++;
                }
            }
        }
        vector<int>ans(15,0);
        for (int i=0;i<n;i++) {
            for (int j=14;j>=0;j--) {
                if (nums[i]&(1<<j)) {
                    ans[14-j]++;
                }
            }
        }
        
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{2,11,4};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.largestPower(nums)<<endl;
    return 0;
}
