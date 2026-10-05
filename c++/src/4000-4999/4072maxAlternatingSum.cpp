// 给你一个整数数组 nums。

// 你最多可以从 nums 中删除 一个 元素，然后在剩下数组里选一个 子数组 。

// 返回所选子数组的最大可能 交替和 。

// 子数组 是数组中连续的 非空 元素序列。

// 数组的 交替和 是其偶数下标处元素之和减去奇数下标处元素之和。在计算其交替和之前，所选子数组会从 0 开始重新编下标。

 

// 示例 1：

// 输入： nums = [5,-5,1]

// 输出： 11

// 解释：

// 选择不删除元素，并选择整个数组。其交替和为 5 - (-5) + 1 = 11，这是最大可能的值。

// 示例 2：

// 输入： nums = [10,-5,-100]

// 输出： 110

// 解释：

// 删除 nums[1] = -5 得到 [10,-100]，然后选择整个所得数组。其交替和为 10 - (-100) = 110，这是最大可能的值。

// 示例 3：

// 输入： nums = [4,7]

// 输出： 7

// 解释：

// 选择不删除元素，并选择子数组 [7]。其交替和为 7，这是最大可能的值。

 

// 提示：

// 1 <= nums.length <= 105
// -105 <= nums[i] <= 105

#include "lc_pub.h"

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n=nums.size();
        vector<long long> end0(n, 0),end1(n, 0);  // end0[i] 以 nums[i] 结尾长度为偶数的最大子数组, end1[i] 以 nums[i] 结尾长度为奇数的最大子数组
        int flg=1;
        long long mn = 0,mx=INT_MIN;
        long long s=0;
        long long ans=nums[0];
        for (int i=0;i<n;i++) {
            s+=nums[i]*flg;
            // s-mn 是偶数下标开头的子数组， s-mx 是奇数下标开头的子数组（需要取反才是可能的最大值）
            if (i%2) {
                end1[i]=-(s-mx);
                end0[i]=s-mn;
                mn=min(mn, s);  // 奇数下标的前缀和
            }
            else {
                end0[i]=-(s-mx);
                end1[i]=s-mn;
                mx=max(mx, s);  // 偶数下标的前缀和
            }

            ans=max(ans,end0[i]);
            ans=max(ans,end1[i]);
            flg=-flg;
        }

        // 从后向前处理，
        // 目标是计算 start1[i]: 子数组符号取反，以 nums[i] 开头的最大子数组，
        //           start0[i]: 保持子数组符号，以 nums[i] 开头的最大子数组
        vector<long long>  start1(n), start0(n);
        if (n%2) flg=1;
        else flg=-1;
        s=0;
        mn=mx = 0;
        for (int i=n-1;i>0;i--) {
            s+=nums[i]*flg;
            start0[i]=s-mn;
            mn = min(mn, s);
            flg=-flg;
        }

        if (n%2) flg=-1;
        else flg=1;
        s=0;
        mn=mx = 0;
        for (int i=n-1;i>0;i--) {
            s+=nums[i]*flg;
            start1[i]=s-mn;
            mn=min(mn,s);
            flg=-flg;
        }

        // 枚举删除一个元素
        for (int i=1;i<n-1;i++) {
            if ((i+1)%2) {
                ans=max(ans,end0[i-1]+start1[i+1]);
                ans=max(ans,end1[i-1]+start0[i+1]);  // 前面长度为奇数，后面要接一个取反的子数组
            }
            else {
                ans=max(ans,end0[i-1]+start0[i+1]);
                ans=max(ans,end1[i-1]+start1[i+1]);  // 前面长度为奇数，后面要接一个取反的子数组
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.maxAlternatingSum(nums)<<endl;
    return 0;
}
