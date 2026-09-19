// 给你一个整数数组 nums。

// 如果一个整数 x 满足以下条件，则被称为 特别 的：

// x 在 nums 中 恰好出现三次。
// x 的 所有 三次出现，在 nums 中都是 等间隔 的。换句话说，如果 x 的所有出现位置的下标为 i1 < i2 < i3，那么 i2 - i1 = i3 - i2。
// 返回 nums 中 不同 特别整数的数量。

 

// 示例 1:

// 输入: nums = [1,8,1,5,1,5,8,5]

// 输出: 2

// 解释:

// 1 是特别的，因为它恰好出现三次，且出现的等间隔下标为 0、2 和 4。
// 5 是特别的，因为它恰好出现三次，且出现的等间隔下标为 3、5 和 7。
// 8 不是特别的，因为它只出现了两次。
// 因此，答案是 2。

// 示例 2:

// 输入: nums = [8,8,8,8]

// 输出: 0

// 解释:

// 8 不是特别的，因为它出现的次数不是恰好三次。因此，答案是 0。

// 示例 3:

// 输入: nums = [8,6,6,8,8]

// 输出: 0

// 解释:

// 8 出现的下标为 0、3 和 4，这些下标不是等间隔的。6 只出现了两次。因此，没有整数是特别的。

 

// 提示:

// 3 <= nums.length <= 100
// 1 <= nums[i] <= 100

#include "lc_pub.h"

class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int, vector<int>> classes;
        int n=nums.size();
        for (int i=0;i<n;i++) {
            classes[nums[i]].push_back(i);
        }
        int ans=0;
        for (auto &[k, ids]: classes) {
            if (ids.size()!=3) continue;
            if (ids[2]-ids[1]==ids[1]-ids[0]) ans++;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{10,12,14,16};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
