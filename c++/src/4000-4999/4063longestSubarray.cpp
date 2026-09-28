// 给你一个整数数组 nums 和一个整数 k。

// 如果一个子数组的和能够被 k 整除，或者在 将该子数组中的一个元素取反 后能使和被 k 整除，则称该子数组是 有效的 。

// 将一个元素取反意味着将其值 x 替换为 -x。

// 返回 最长有效子数组的长度 。如果不存在有效的子数组，则返回 0。

// 子数组 是数组中一个连续且非空的元素序列。

 

// 示例 1：

// 输入： nums = [4,1,2], k = 3

// 输出： 3

// 解释：

// 整个数组的和为 7，且 7 % 3 = 1，因此它不能被 k = 3 整除。
// 将 nums[2] = 2 取反，其和变为 4 + 1 − 2 = 3，能够被 k 整除。
// 因此，整个数组是一个有效子数组，其长度为 3。
// 示例 2：

// 输入： nums = [5,3,4], k = 7

// 输出： 2

// 解释：

// 整个数组的和为 12，且将其中任何一个元素取反都无法使其和被 7 整除。
// 然而，子数组 [3, 4] 的和为 7，无需任何取反操作即可被 k = 7 整除。
// 因此，最长有效子数组的长度为 2。
// 示例 3：

// 输入： nums = [2,2,5], k = 6

// 输出： 2

// 解释：

// 整个数组的和为 9，且将其中任何一个元素取反都无法使其和被 6 整除。
// 子数组 [2, 2] 的和为 4。将其中任意一个元素取反会使其变为 [-2, 2] 或 [2, -2]，这两者的和皆为 0。
// 因此，最长有效子数组的长度为 2。
 

// 提示：

// 1 <= nums.length <= 1000
// -105 <= nums[i] <= 105
// 1 <= k <= 105

#include "lc_pub.h"

class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int n=nums.size();
        int ans=0;
        for (int l=0;l<n;l++) {  // 都变成正数进行处理
            if (nums[l]<0)
                nums[l]=nums[l]%k+k;
        }
        for (int l=0;l<n;l++) {
            unordered_set<int> mod_k;  // 存放 每个元素的2倍模k的值，
            int s=0;   // [l,r] 区间和
            for (int r=l;r<n;r++) {
                s+=nums[r];
                if (s%k==0) {
                    ans=max(ans,r-l+1);
                }
                mod_k.insert((nums[r]*2)%k);
                int mods=s%k;
                if (mod_k.find(mods)!=mod_k.end()) {  // 区间中如果有个元素的2倍模k的值，恰好等于s模k的值，那么它们相减就整除k
                    ans=max(ans,r-l+1);
                }
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-10,-21,-7};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.longestSubarray(nums,13)<<endl;
    return 0;
}
