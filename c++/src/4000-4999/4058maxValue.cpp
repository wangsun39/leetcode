// 给你一个长度为 n 的整数数组 nums。

// 定义整数数组 arr 的 脉冲值 为从下标 0 开始的 交替和 ：pulse(arr) = arr[0] - arr[1] + arr[2] - arr[3] + ...

// 你可以对 nums 执行 至多一次 操作：

// 选择两个下标 l 和 r，满足 0 <= l < r <= n - 1。
// 将子数组 nums[l..r] 循环左移恰好 一个位置。例如，[a, b, c, d] 变为 [b, c, d, a]。
// 返回执行 至多一次 该操作后可以获得的 最大脉冲值。

// 子数组 是数组中连续且 非空 的元素序列。

 

// 示例 1：

// 输入：nums = [1,5,2]

// 输出：6

// 解释：

// 原始脉冲值为 1 - 5 + 2 = -2。
// 将子数组 nums[0..1] 从 [1, 5] 循环左移为 [5, 1]。
// 得到的数组为 [5, 1, 2]，其脉冲值为 5 - 1 + 2 = 6，这是可能的最大值。
// 示例 2：

// 输入：nums = [6,4,3]

// 输出：7

// 解释：

// 原始脉冲值为 6 - 4 + 3 = 5。
// 将子数组 nums[1..2] 从 [4, 3] 循环左移为 [3, 4]。
// 得到的数组为 [6, 3, 4]，其脉冲值为 6 - 3 + 4 = 7，这是可能的最大值。
// 示例 3：

// 输入：nums = [9,7]

// 输出：2

// 解释：

// 原始脉冲值为 9 - 7 = 2，已经是最大值。因此，不需要进行旋转操作。

 

// 提示：

// 1 <= n == nums.length <= 105
// -109 <= nums[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    long long maxValue(vector<int>& nums) {
        long long mx0=0,mx1=INT64_MIN;
        int n=nums.size();
        vector<long long> s(n+1, 0);
        int flg=1;
        for (int i=0;i<n;i++) {
            s[i+1]=s[i]+nums[i]*flg;
            flg=-flg;
        }
        long long ans=s[n];
        for (int i=0;i<n;i++) {
            long long diff=0;
            if (i&1) {
                diff=s[i+1]-mx0;
                mx0=max(mx0, s[i+1]);
            }
            else {
                if (mx1!=INT64_MIN)
                    diff=s[i+1]-mx1;
                mx1=max(mx1, s[i+1]);
            }
            if (diff<0)
                ans=max(ans, s[n]-diff*2);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,5,2};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maxValue(nums)<<endl;
    return 0;
}
