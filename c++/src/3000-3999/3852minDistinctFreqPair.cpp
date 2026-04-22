// 给你一个整数数组 nums。

// 从 nums 中找出两个 互不相同 的值 x 和 y，使得：

// x < y
// x 和 y 在 nums 中的频率不同。
// 在所有满足条件的数对中：

// 选择 x 的值尽可能小的数对。
// 如果存在多个 x 相同的数对，选择 y 的值尽可能小的那个。
// 返回一个整数数组 [x, y]。如果不存在有效的数对，返回 [-1, -1]。

// 一个值 x 的 频率 是指它在数组中出现的次数。

 

// 示例 1：

// 输入： nums = [1,1,2,2,3,4]

// 输出： [1,3]

// 解释：

// 最小的值是 1，频率为 2。比 1 大且频率与 1 不同的最小值是 3，其频率为 1。因此，答案是 [1, 3]。

// 示例 2：

// 输入： nums = [1,5]

// 输出： [-1,-1]

// 解释：

// 两个值的频率相同，因此不存在有效的数对。返回 [-1, -1]。

// 示例 3：

// 输入： nums = [7]

// 输出： [-1,-1]

// 解释：

// 数组中只有一个值，因此不存在有效的数对。返回 [-1, -1]。

 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 100

#include "lc_pub.h"

class Solution {
public:
    vector<int> minDistinctFreqPair(vector<int>& nums) {
        map<int, int> counter;
        for (int x: nums) {
            counter[x]++;
        }
        for (auto it=counter.begin();it!=counter.end();it++) {
            auto it1=it;
            for (++it1;it1!=counter.end();it1++) {
                if (it->second!=it1->second) return {it->first,it1->first};
            }
        }
        return {-1,-1};
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
