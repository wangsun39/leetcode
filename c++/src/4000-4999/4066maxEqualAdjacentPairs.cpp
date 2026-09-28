// 给你一个 下标从 1 开始 的整数数组 nums。

// 你可以选择两个 不同 的值 x 和 y，并 最多 执行一次以下操作：

// 将 nums 中所有值为 x 的元素替换为 y。
// 返回执行操作后，相邻且相等的元素对数量的 最大值 。

 

// 示例 1：

// 输入： nums = [1,2,3,2]

// 输出： 2

// 解释：

// 一种最优方案是选择 x = 3 和 y = 2。
// 得到的数组为 [1, 2, 2, 2]。
// 有 2 对相邻且相等的元素：(nums[2], nums[3]) 和 (nums[3], nums[4])。
// 因此，答案为 2。
// 示例 2：

// 输入： nums = [1,2,1,2,1]

// 输出： 4

// 解释：

// 一种最优方案是选择 x = 1 和 y = 2。
// 得到的数组为 [2, 2, 2, 2, 2]。
// 有 4 对相邻且相等的元素：(nums[1], nums[2])、(nums[2], nums[3])、(nums[3], nums[4]) 和 (nums[4], nums[5])。
// 因此，答案为 4。
// 示例 3：

// 输入： nums = [1,1,1]

// 输出： 2

// 解释：

// 一种最优方案是不执行任何操作。
// 因此，得到的数组仍为 [1, 1, 1]。
// 有 2 对相邻且相等的元素：(nums[1], nums[2]) 和 (nums[2], nums[3])。
// 因此，答案为 2。
 

// 提示：

// 2 <= nums.length <= 105
// 1 <= nums[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    int maxEqualAdjacentPairs(vector<int>& nums) {
        unordered_map<long long, int> counter;
        int o_ans=0;
        int n=nums.size();
        for (int i=1;i<n;i++) {
            long long key=0;
            if (nums[i-1]>nums[i]) {
                key = (((long long)nums[i]) << 32) | nums[i - 1];
            }
            else {
                key = (((long long)nums[i - 1]) << 32) | nums[i];
            }
            counter[key]++;
            if (nums[i-1]==nums[i]) o_ans++;
        }
        int ans = o_ans;

        for (auto &[k, v]: counter) {
            int a=k>>32,b=k;
            if (a==b) continue;
            ans = max(ans,v+o_ans);
        }

        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{7,7,3,3};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maxEqualAdjacentPairs(nums)<<endl;
    return 0;
}
