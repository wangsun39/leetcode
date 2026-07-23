// 给你一个整数数组 nums 和两个整数 a 和 b，满足 a < b。

// 如果一个数组可以按顺序分成三个 连续 的部分，并且满足以下条件，则称其为 好数组：

// 第一部分中的每个元素都 小于 a。
// 第二部分中的每个元素都 在 闭区间 [a, b] 内。
// 第三部分中的每个元素都 大于 b。
// 这三个部分中的任意一个都 可以 为空。

// 在一次 相邻交换 中，你可以交换 nums 的两个 相邻 元素。

// 返回使 nums 成为好数组所需的 最少 相邻交换次数。由于答案可能非常大，请将其对 109 + 7 取余 后返回。

 

// 示例 1：

// 输入： nums = [1,3,2,4,5,6], a = 3, b = 4

// 输出： 1

// 解释：

// 交换 nums[1] 和 nums[2]。数组变为 [1, 2, 3, 4, 5, 6]。
// 这个数组是好数组，因为它可以分为 [1, 2]、[3, 4] 和 [5, 6]。
// 示例 2：

// 输入： nums = [9,7,5,3], a = 4, b = 8

// 输出： 5

// 解释：

// 一种最佳交换序列如下：

// 交换 nums[2] 和 nums[3]。数组变为 [9, 7, 3, 5]。
// 交换 nums[1] 和 nums[2]。数组变为 [9, 3, 7, 5]。
// 交换 nums[0] 和 nums[1]。数组变为 [3, 9, 7, 5]。
// 交换 nums[1] 和 nums[2]。数组变为 [3, 7, 9, 5]。
// 交换 nums[2] 和 nums[3]。数组变为 [3, 7, 5, 9]。
// 这个数组是好数组，因为它可以分为 [3]、[7, 5] 和 [9]。
// 示例 3：

// 输入： nums = [3,7,5,9], a = 4, b = 8

// 输出： 0

// 解释：

// 该数组已经是好数组。不需要交换。

 

// 提示：

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 109
// 1 <= a < b <= 109

#include "lc_pub.h"

class Solution {
public:
    int minAdjacentSwaps(vector<int>& nums, int a, int b) {
        int n1=0,n2=0,n3=0,n=nums.size();
        int MOD=1E9+7;
        for (int i=0;i<n;i++) {
            if (nums[i]<a) n1++;
            else if (nums[i]>b) n3++;
            else n2++;
        }
        int g_a=0,g_b=0;  // 遍历过程中有多少个数比a大，以及有多少数比a大且比b小
        long long ans=0;
        // 先把应属于第一段的数都交换到第一段
        for (int i=0;i<n;i++) {
            if (nums[i]>=a) {
                g_a++;
            }
            else { // 第一段的数，要与所有g_a个数交换
                ans+=g_a;
                ans%=MOD;
            }
        }
        // 再把应属于第三段的数都交换到第三段
        for (int i=n-1;i>=0;i--) {
            if (nums[i]>=a&&nums[i]<=b) {
                g_b++;
            }
            else if (nums[i]>b) { // 第三段的数，要与所有g_b个数交换
                ans+=g_b;
                ans%=MOD;
            }
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
    cout<<so.minAdjacentSwaps(nums, 3,4);
    return 0;
}
