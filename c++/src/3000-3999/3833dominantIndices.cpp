// 给你一个长度为 n 的整数数组 nums。

// 当下标 i 满足以下条件时，该下标处的元素被称为 主导元素：nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])

// 你的任务是统计数组中 主导元素 的下标数。

// 平均值 是指一组数的总和除以该组数的个数得到的值。

// 注意：数组的 最右边元素 不算作 主导元素 。

 

// 示例 1：

// 输入： nums = [5,4,3]

// 输出： 2

// 解释：

// 在下标 i = 0 处，值 5 是主导元素，因为 5 > average(4, 3) = 3.5。
// 在下标 i = 1 处，值 4 是主导元素，相对于子数组 [3]。
// 下标 i = 2 不是主导元素，因为它右侧没有元素。因此答案是 2。
// 示例 2：

// 输入： nums = [4,1,2]

// 输出： 1

// 解释：

// 在下标 i = 0 处，值 4 是主导元素，相对于子数组 [1, 2]。
// 在下标 i = 1 处，值 1 不是主导元素。
// 下标 i = 2 不是主导元素，因为它右侧没有元素。因此答案是 1。
 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 100​​​​​​​

#include "lc_pub.h"

class Solution {
public:
    int dominantIndices(vector<int>& nums) {
        int n=nums.size();
        long long s=0;
        int ans=0;
        for (int i=n-2;i>=0;i--) {
            s+=nums[i+1];
            if (nums[i]*(n-i-1)>s) ans++;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
