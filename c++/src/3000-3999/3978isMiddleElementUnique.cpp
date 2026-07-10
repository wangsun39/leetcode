// 给你一个长度为 n 的整数数组 nums 和一个整数 k 。

// 如果满足以下条件，则下标对 (i, j) 被称为 有效 的：

// 0 <= i < j < n
// j - i >= k
// 返回所有有效对中的 nums[i] + nums[j] 的 最大 值。

 

// 示例 1：

// 输入： nums = [1,3,5,2,8], k = 2

// 输出： 13

// 解释：

// 有效对为：

// (0, 2): nums[0] + nums[2] = 6
// (0, 3): nums[0] + nums[3] = 3
// (0, 4): nums[0] + nums[4] = 9
// (1, 3): nums[1] + nums[3] = 5
// (1, 4): nums[1] + nums[4] = 11
// (2, 4): nums[2] + nums[4] = 13
// 因此，答案为 13 。

// 示例 2：

// 输入： nums = [5,1,9], k = 1

// 输出： 14

// 解释：

// 因为 k = 1 ，每一对都是有效的。
// 最大值由对 (0, 2) 取得，为 nums[0] + nums[2] = 5 + 9 = 14 。
// 因此，答案为 14 。
 

// 提示：

// 2 <= n == nums.length <= 105
// 1 <= nums[i] <= 109
// 1 <= k <= n - 1

#include "lc_pub.h"


class Solution {
public:
    bool isMiddleElementUnique(vector<int>& nums) {
        int n=nums.size();
        int m=nums[n/2];
        for (int i=0;i<n/2;i++) {
            if (nums[i]==m||nums[n-1-i]==m) return false;
        }
        return true;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
