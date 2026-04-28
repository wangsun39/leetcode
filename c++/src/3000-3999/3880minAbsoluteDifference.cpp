// 给你一个只包含 0、1 和 2 的整数数组 nums。

// 如果 nums[i] == 1 且 nums[j] == 2，则称下标对 (i, j) 为 有效 的。

// 请返回所有有效下标对中 i 和 j 之间的 最小 绝对差。如果不存在有效下标对，则返回 -1。

// 下标 i 和 j 之间的绝对差定义为 abs(i - j)。

 

// 示例 1：

// 输入： nums = [1,0,0,2,0,1]

// 输出： 2

// 解释：

// 有效下标对有：

// (0, 3)，其绝对差为 abs(0 - 3) = 3。
// (5, 3)，其绝对差为 abs(5 - 3) = 2。
// 因此，结果是 2。

// 示例 2：

// 输入： nums = [1,0,1,0]

// 输出： -1

// 解释：

// 数组中不存在有效下标对，因此结果是 -1。

 

// 提示：

// 1 <= nums.length <= 100
// 0 <= nums[i] <= 2

#include "lc_pub.h"

class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums) {
        int pre2=-1,pre1=-1,n=nums.size();
        int ans=n;
        for (int i=0;i<n;i++) {
            if (nums[i]==2) {
                if (pre1!=-1) ans=min(ans,i-pre1);
                pre2=i;
            }
            else if (nums[i]==1) {
                if (pre2!=-1) ans=min(ans,i-pre2);
                pre1=i;
            }
        }
        return ans==n?-1:ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
