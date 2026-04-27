// 给你一个整数数组 nums。

// 请你返回一个整数，表示 nums 中出现 恰好 一次的第一个 偶数（以数组下标最早为准）。如果不存在这样的整数，返回 -1。

// 如果一个整数 x 能被 2 整除，那么它就被认为是 偶数。

 

// 示例 1：

// 输入： nums = [3,4,2,5,4,6]

// 输出： 2

// 解释：

// 2 和 6 都是偶数，并且它们都恰好出现一次。因为 2 在数组中出现得更早，所以答案是 2。

// 示例 2：

// 输入： nums = [4,4]

// 输出： -1

// 解释：

// 没有恰好出现一次的偶数，所以返回 -1。

 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 100

#include "lc_pub.h"

class Solution {
public:
    int firstUniqueEven(vector<int>& nums) {
        unordered_map<int,int> c;
        for (int x: nums) {
            c[x]++;
        }
        for (int x: nums)
            if ((x&1)==0&&c[x]==1) return x;
        return -1;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
