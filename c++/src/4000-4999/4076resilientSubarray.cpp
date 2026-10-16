// 给你一个整数数组 nums 和一个整数 k。

// 如果对一个子数组中的 每一个 元素，删除 该元素后，剩余 元素的 和能被 k 整除 ，那么称它是 有韧性的 。

// 对于长度为 1 的子数组，剩余元素的和为 0，可以被 k 整除。

// 返回 最长有韧性子数组 的长度。

// 子数组 是数组中连续的 非空 元素序列。

 

// 示例 1：

// 输入： nums = [2,4,6,3], k = 2

// 输出： 3

// 解释：

// 子数组 [2, 4, 6] 的和为 12，删除 2、4 和 6 后的剩余和分别为 10、8 和 6，它们都能被 2 整除。因此，答案是 3。

// 示例 2：

// 输入： nums = [1,4,7,1], k = 3

// 输出： 4

// 解释：

// 子数组 [1, 4, 7, 1] 的和为 13，删除 1、4、7 和 1 后的剩余和分别为 12、9、6 和 12，它们都能被 3 整除。因此，答案是 4。

// 示例 3：

// 输入： nums = [5,5,4,8], k = 4

// 输出： 2

// 解释：

// [5, 5] 不是有韧性的，因为删除任意一个 5 都会剩下 5，而 5 不能被 4 整除。

// 子数组 [4, 8] 的和为 12，删除 4 和 8 后的剩余和分别为 8 和 4，它们都能被 4 整除。因此，答案是 2。

 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 105
// 1 <= k <= 105

#include "lc_pub.h"

class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int n=nums.size();
        vector<int> re(n, 0);
        unordered_map<int,int> stat;  // 记录某个余数的最大连续个数
        int pre=-1;
        for (int i=0;i<n;i++) {
            re[i]=nums[i]%k;
            if (i) {
                if (re[i]==re[i-1]) {
                    stat[re[i]]=max(stat[re[i]],i-pre+1);
                }
                else {
                    pre=i;
                    stat[re[i]]=max(stat[re[i]],1);
                }
            }
            else {
                pre=i;
                stat[re[i]]=1;
            }
        }
        int ans=0;
        for (auto &[r, v]: stat) {
            // 连续v个余数为r的子数组，能产生符合要求的最大的子数组长度
            // 这段子数组和模k也需要余r
            for (int i=v;i>0;i--) {
                if ((r * i) % k == r) {
                    ans=max(ans, i);
                    break;
                }
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
