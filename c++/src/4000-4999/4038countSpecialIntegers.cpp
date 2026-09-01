// 给你一个整数数组 nums。

// 如果整数 x 在 nums 中的所有出现位置都位于同一个 连续 区间内，则称 x 为 特殊整数。

// 返回 nums 中 不同 特殊整数的数量。

 

// 示例 1：

// 输入： nums = [1,2,2,1]

// 输出： 1

// 解释：

// 1 出现在下标 0 和 3，形成了两个分离的区间，因此它不是特殊整数。
// 2 在下标 [1, 2] 处形成一个连续区间，因此它是特殊整数。
// 因此，共有一个特殊整数。

// 示例 2：

// 输入： nums = [3,3,1,2,2,1]

// 输出： 2

// 解释：

// 3 在下标 [0, 1] 处形成一个连续区间，因此它是特殊整数。
// 1 出现在下标 2 和 5，形成了两个分离的区间，因此它不是特殊整数。
// 2 在下标 [3, 4] 处形成一个连续区间，因此它是特殊整数。
// 因此，共有两个特殊整数。

 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 100

#include "lc_pub.h"

class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_set<int>ans;
        unordered_set<int>exist;
        int n=nums.size();
        ans.insert(nums[0]);
        exist.insert(nums[0]);
        for (int i=1;i<n;i++) {
            if (nums[i]==nums[i-1]) continue;
            if (exist.find(nums[i])!=exist.end()) {
                ans.erase(nums[i]);
                continue;
            }
            exist.insert(nums[i]);
            ans.insert(nums[i]);
        }
        return ans.size();
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> pa{-1,0,0,0,2,2};
    vector<int> nums{67108864,9,7};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
